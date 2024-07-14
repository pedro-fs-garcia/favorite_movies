document.addEventListener("DOMContentLoaded", function () {
    // Selecione todos os botões de rádio
    const radioButtons = document.querySelectorAll('input[name="chooseoption"]');

    radioButtons.forEach(radio => {
        radio.addEventListener('change', function () {
            // Remova a borda vermelha de todas as divs
            document.getElementById("option1label").classList.remove('selected-border');
            document.getElementById("option2label").classList.remove('selected-border');

            // Adicione a borda vermelha à div correspondente ao botão de rádio selecionado
            if (radio.checked) {
                document.querySelector(`label[for="${radio.id}"] .film_box`).classList.add('selected-border');
            }
        });
    });
});


