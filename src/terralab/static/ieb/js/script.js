document.addEventListener('DOMContentLoaded', function () {
    const urlContainer = document.getElementById('url-container');
    
    // Verificar se o container de URLs está presente
    if (!urlContainer) {
        console.error('Elemento url-container não encontrado no DOM. Verifique se o HTML está corretamente configurado.');
        return;
    }

    // URLs dinâmicas passadas do HTML, utilizando um fallback para evitar referências indefinidas
    const urlComponentes = urlContainer.dataset.urlComponentes || '';
    const urlEquipes = urlContainer.dataset.urlEquipes || '';
    const urlEquipesAdicionais = urlContainer.dataset.urlEquipesAdicionais || '';
    const urlAtividades = urlContainer.dataset.urlAtividades || '';
    const urlIndicadores = urlContainer.dataset.urlIndicadores || '';

    // Verificar se todas as URLs necessárias estão disponíveis
    if (!urlComponentes || !urlEquipes || !urlEquipesAdicionais || !urlAtividades || !urlIndicadores) {
        console.error('Algumas URLs necessárias não foram encontradas. Verifique se todos os atributos data-url estão presentes no elemento url-container.');
        return;
    }

    // Função para normalizar as chaves
    function normalizeKey(key) {
        return key.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/ /g, "_");
    }

    // Normalizar as chaves do `indicadoresConfig`
    const normalizedIndicadoresConfig = {};
    for (let key in indicadoresConfig) {
        const normalizedKey = normalizeKey(key);
        normalizedIndicadoresConfig[normalizedKey] = indicadoresConfig[key];
    }

    // Logar todas as chaves disponíveis em `indicadoresConfig`
    console.log("Chaves disponíveis em normalizedIndicadoresConfig:", Object.keys(normalizedIndicadoresConfig));

    // Ao mudar o projeto, carregar componentes, equipes e equipes adicionais
    document.getElementById('id_projeto').addEventListener('change', function() {
        console.log("Projeto selecionado:", this.value);
        if (urlComponentes) {
            var url = urlComponentes + "?projeto=" + this.value;
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log("Componentes recebidos:", data);
                    var select = document.getElementById('id_componente');
                    select.innerHTML = '<option value="">Selecione um componente</option>';
                    data.forEach(item => {
                        select.innerHTML += '<option value="' + item.id + '">' + item.nome + '</option>';
                    });
                });
        }

        if (urlEquipes) {
            var equipes_url = urlEquipes + "?projeto=" + this.value;
            fetch(equipes_url)
                .then(response => response.json())
                .then(data => {
                    console.log("Equipes recebidas:", data);
                    var select = document.getElementById('id_equipe_projeto');
                    select.innerHTML = '<option value="">Selecione uma equipe</option>';
                    data.forEach(item => {
                        select.innerHTML += '<option value="' + item.id + '">' + item.nome + '</option>';
                    });
                });
        }

        if (urlEquipesAdicionais) {
            var equipes_adicionais_url = urlEquipesAdicionais + "?projeto=" + this.value;
            fetch(equipes_adicionais_url)
                .then(response => response.json())
                .then(data => {
                    console.log("Equipes adicionais recebidas:", data);
                    var checkboxGroup = document.getElementById('id_equipe_adicional');
                    
                    if (checkboxGroup) {
                        checkboxGroup.innerHTML = '';
                        data.forEach(item => {
                            checkboxGroup.innerHTML += '<label><input type="checkbox" name="equipe_adicional" value="' + item.id + '"> ' + item.nome + '</label>';
                        });
                    }
                });
        }
    });

    // Ao mudar o componente, carregar atividades
    document.getElementById('id_componente').addEventListener('change', function() {
        console.log("Componente selecionado:", this.value);
        if (urlAtividades) {
            var url = urlAtividades + "?componente=" + this.value;
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log("Atividades recebidas:", data);
                    var select = document.getElementById('id_atividade');
                    select.innerHTML = '<option value="">Selecione uma atividade</option>';
                    data.forEach(item => {
                        select.innerHTML += '<option value="' + item.id + '">' + item.nome + '</option>';
                    });
                });
        }
    });

    // Ao mudar a atividade, carregar indicadores
    document.getElementById('id_atividade').addEventListener('change', function() {
        console.log("Atividade selecionada:", this.value);
        if (urlIndicadores) {
            const url = urlIndicadores + "?atividade=" + this.value;
            
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log("Indicadores recebidos:", data);
                    const indicadoresDiv = document.getElementById('indicadores');
                    
                    if (indicadoresDiv) {
                        indicadoresDiv.innerHTML = ''; // Limpar indicadores anteriores

                        data.forEach(item => {
                            const indicadorKey = normalizeKey(item.nome);
                            
                            console.log(`Tentando acessar indicador com a chave: "${indicadorKey}"`);
                            
                            if (normalizedIndicadoresConfig[indicadorKey]) {
                                console.log("Renderizando indicador:", item.nome);
                                indicadoresDiv.innerHTML += `<div class="indicator-section"><h3>${item.nome}</h3>`;

                                normalizedIndicadoresConfig[indicadorKey].forEach(field => {
                                    const fieldName = `indicadores_${item.id}_${field.name}`;
                                    if (field.type === 'number' || field.type === 'text') {
                                        indicadoresDiv.innerHTML += `
                                            <div>
                                                <label>${field.label}:</label>
                                                <input type="${field.type}" name="${fieldName}" placeholder="${field.label}">
                                            </div>
                                        `;
                                    } else if (field.type === 'select') {
                                        let optionsHTML = '';
                                        field.options.forEach(option => {
                                            optionsHTML += `
                                                <div style="display: flex; align-items: center; margin-bottom: 5px;">
                                                    <input type="radio" id="${fieldName}_${option.value}" name="${fieldName}" value="${option.value}" style="margin-right: 5px;">
                                                    <label for="${fieldName}_${option.value}" style="font-size: 14px;">${option.label}</label>
                                                </div>
                                            `;
                                        });
                                        indicadoresDiv.innerHTML += `
                                            <div>
                                                <label>${field.label}:</label>
                                                ${optionsHTML}
                                            </div>
                                        `;
                                    } else if (field.type === 'checkbox') {
                                        renderCheckboxField(field, fieldName, indicadoresDiv);
                                    }
                                });

                                indicadoresDiv.innerHTML += `</div>`; // Fechar a seção do indicador
                            } else {
                                console.warn(`Indicador não encontrado na configuração: "${indicadorKey}". Verifique se a configuração de indicadores está correta.`);
                            }
                        });
                    } else {
                        console.error("Elemento de indicadores não encontrado no DOM.");
                    }
                })
                .catch(error => {
                    console.error('Erro ao carregar indicadores:', error);
                });
        }
    });

    // Função para renderizar checkbox
    function renderCheckboxField(field, fieldName, indicadoresDiv) {
        console.log("Renderizando checkbox para campo:", fieldName);
        let optionsHTML = '';
        field.options.forEach(option => {
            optionsHTML += `
                <div style="display: flex; align-items: center; margin-bottom: 5px;">
                    <input type="checkbox" id="${fieldName}_${option.value}" name="${fieldName}" value="${option.value}" style="margin-right: 5px;">
                    <label for="${fieldName}_${option.value}" style="font-size: 14px;">${option.label}</label>
                </div>
            `;
        });
        indicadoresDiv.innerHTML += `
            <div>
                <label>${field.label}:</label>
                ${optionsHTML}
            </div>
        `;
    }

    // Função para gerar UUID (substituto para `crypto.randomUUID()` se não for suportado)
    function generateUUID() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    const form = document.querySelector('form');
    const requiredFields = form.querySelectorAll('input[required], select[required], textarea[required]');

    // Função para validar campos
    function validateField(field) {
        if (!field.value.trim()) {
            field.classList.add('invalid');
            field.classList.remove('valid');
        } else {
            field.classList.remove('invalid');
            field.classList.add('valid');
        }
    }

    // Valida todos os campos obrigatórios no carregamento da página
    requiredFields.forEach(validateField);

    form.addEventListener('submit', function(event) {
        let allValid = true;

        requiredFields.forEach(field => {
            validateField(field);
            if (field.classList.contains('invalid')) {
                allValid = false;
            }
        });

        if (!allValid) {
            event.preventDefault(); // Impede o envio do formulário se houver campos inválidos
        }
    });

    requiredFields.forEach(field => {
        field.addEventListener('input', function() {
            validateField(field);
        });
    });
});
