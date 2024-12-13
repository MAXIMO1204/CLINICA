// nav background
let header = document.querySelector("header");

window.addEventListener("scroll", () => {
    header.classList.toggle("shadow", window.scrollY > 0)
})

//Filter
$(document).ready(function () {
    $(".filter-item").click(function () {
        const value = $(this).attr("data-filter");
        if (value == "all"){
            $(".post-box").show("1000")
        } else{
            $(".post-box")
                .not("." + value)
                .hide(1000);
            $(".post-box")
            .filter("." + value)
            .show("1000")
        }
    });
    $(".filter-item").click(function () {
        $(this).addClass("active-filter").siblings().removeClass("active-filter")
    });
});


function editarMedico(id) {
    // Redirige a la página de edición con el ID del médico
    window.location.href = 'form_medico.php?id=' + id;
}

function eliminarMedico(id) {
    if (confirm('¿Estás seguro de que deseas eliminar este médico?')) {
        var form = document.createElement('form');
        form.method = 'POST';
        form.action = 'crud.php';

        var inputId = document.createElement('input');
        inputId.type = 'hidden';
        inputId.name = 'id';
        inputId.value = id;

        var inputAccion = document.createElement('input');
        inputAccion.type = 'hidden';
        inputAccion.name = 'accion';
        inputAccion.value = 'eliminar';

        form.appendChild(inputId);
        form.appendChild(inputAccion);

        document.body.appendChild(form);
        form.submit();
    }
}
document.querySelectorAll('.carousel-control-prev, .carousel-control-next').forEach(control => {
    control.addEventListener('click', event => {
        event.preventDefault();
    });
});

   


  












