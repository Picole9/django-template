if (localStorage.getItem("django-theme") === null) {
    // read browser preferences
    if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
        setTheme("dark");
    } else {
        setTheme("light");
    }
} else {
    setTheme(localStorage.getItem("django-theme"));
}

// buttonlistener darkmode
document.getElementById('colorIcon').addEventListener('click',()=>{
    if (localStorage.getItem("django-theme") === "dark") {
        setTheme("light");
    } else {
        setTheme("dark");
    }
});

function setTheme(mode) {
    switch (mode){
        case "dark":
            document.documentElement.setAttribute('data-bs-theme','dark');
            document.getElementById('colorIcon').className="fa-solid fa-lightbulb";
            c = document.getElementsByClassName("brand");
            for (let i = 0; i < c.length; i++) {
                c.item(i).src = banner_dark;
            }
            localStorage.setItem("django-theme", "dark");
            break;
        case "light":
            document.documentElement.setAttribute('data-bs-theme','light');
            document.getElementById('colorIcon').className="fa-solid fa-moon";
            c = document.getElementsByClassName("brand");
            for (let i = 0; i < c.length; i++) {
                c.item(i).src = banner_light;
            }
            localStorage.setItem("django-theme", "light");
            break;
        default:
            console.log("mode not supported");
    }
}
