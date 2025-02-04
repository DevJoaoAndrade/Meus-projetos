// Essa função serve para selecionarmos um campo de escolha entre pessoa fisica ou juridica
function toggleFields() {
    var tipo = document.getElementById('tipo').value;
    document.getElementById('fisica').style.display = tipo == 'fisica' ? 'block' : 'none';
    document.getElementById('juridica').style.display = tipo == 'juridica' ? 'block' : 'none';
}
