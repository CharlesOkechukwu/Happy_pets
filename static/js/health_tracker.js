// Hide and Display Health Treacker sessions
$(document).ready(function () {
    $(".mini-nav.records").click(function () {
        const petId = $(this).attr('id').split('-')[1];
        $("#records-" + petId).addClass("active");
        $("#growth-" + petId).removeClass("active");
        $("#symptoms-" + petId).removeClass("active");
        $("#track-growth-" + petId).addClass("hide");
        $("#check-symptom-" + petId).addClass("hide");
        $("#health-record-" + petId).removeClass("hide");
    });

    $(".mini-nav.growth").click(function () {
        const petId = $(this).attr('id').split('-')[1];
        $("#records-" + petId).removeClass("active");
        $("#symptoms-" + petId).removeClass("active");
        $("#growth-" + petId).addClass("active");
        $("#track-growth-" + petId).removeClass("hide");
        $("#health-record-" + petId).addClass("hide");
        $("#check-symptom-" + petId).addClass("hide");
    });

    $(".mini-nav.symptoms").click(function () {
        const petId = $(this).attr('id').split('-')[1];
        $("#growth-" + petId).removeClass("active");
        $("#records-" + petId).removeClass("active");
        $("#symptoms-" + petId).addClass("active");
        $("#check-symptom-" + petId).removeClass("hide");
        $("#track-growth-" + petId).addClass("hide");
        $("#health-record-" + petId).addClass("hide");
    });
});