// window.onload is optional since it depends on the way in which you fire events
window.onload = function () {

    // selecting the elements for which we want to add a tooltip
    const target1 = document.getElementById("tooltip-button1");
    const tooltip1 = document.getElementById("tooltip-text1");
    const target2 = document.getElementById("tooltip-button2");
    const tooltip2 = document.getElementById("tooltip-text2");
    const target3 = document.getElementById("tooltip-button3");
    const tooltip3 = document.getElementById("tooltip-text3");
    const target4 = document.getElementById("tooltip-button4");
    const tooltip4 = document.getElementById("tooltip-text4");
    const target5 = document.getElementById("tooltip-button5");
    const tooltip5 = document.getElementById("tooltip-text5");

    // change display to 'block' on mouseover
    target1.addEventListener('mouseover', () => {
        tooltip1.style.display = 'block';
    }, false);

    target2.addEventListener('mouseover', () => {
        tooltip2.style.display = 'block';
    }, false);

    target3.addEventListener('mouseover', () => {
        tooltip3.style.display = 'block';
    }, false);

    target4.addEventListener('mouseover', () => {
        tooltip4.style.display = 'block';
    }, false);

    target5.addEventListener('mouseover', () => {
        tooltip5.style.display = 'block';
    }, false);

    // change display to 'none' on mouseleave
    target1.addEventListener('mouseleave', () => {
        tooltip1.style.display = 'none';
    }, false);

    target2.addEventListener('mouseleave', () => {
        tooltip2.style.display = 'none';
    }, false);

    target3.addEventListener('mouseleave', () => {
        tooltip3.style.display = 'none';
    }, false);

    target4.addEventListener('mouseleave', () => {
        tooltip4.style.display = 'none';
    }, false);

    target5.addEventListener('mouseleave', () => {
        tooltip5.style.display = 'none';
    }, false);

    
}

