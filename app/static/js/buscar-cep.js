// Função que serve para buscar cep em uma aplicação externa
function buscarCep() {
    let cep = document.getElementById('cep').value;
    cep = cep.replace(/\D/g, '');
    if (cep.length !== 8) {
        alert('CEP inválido!');
        return;
    }

    fetch(`/buscar_cep?cep=${cep}`)
        .then(response => response.json())
        .then(data => {
            if (data.erro) {
                document.getElementById('rua').value = "Endereço não encontrado";
                document.getElementById('bairro').value = "Endereço não encontrado";
            } else {
                document.getElementById('rua').value = data.rua;
                document.getElementById('bairro').value = data.bairro;
            }
        })
        .catch(error => console.error('Erro:', error));

}