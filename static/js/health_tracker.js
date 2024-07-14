$(document).ready(function () {
    $("#records").click(function () {
        $("#records").addClass("active");
        $("#growth").removeClass("active");
        $("#symptoms").removeClass('active');
        $("#track-growth").addClass("hide");
        $("#check-symptom").addClass("hide")
        $("#health-record").removeClass("hide");
    });
    $("#growth").click(function () {
        $("#records").removeClass("active");
        $('#symptoms').removeClass('active');
        $("#growth").addClass('active');
        $("#track-growth").removeClass("hide");
        $('#health-record').addClass('hide');
        $("#check-symptom").addClass("hide");
    });
    $("#symptoms").click(function () {
        $("#growth").removeClass("active");
        $("#records").removeClass("active");
        $("#symptoms").addClass('active');
        $("#check-symptom").removeClass("hide");
        $("#track-growth").addClass("hide");
        $("#health-record").addClass("hide");
    });
});