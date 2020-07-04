var inside_sidebar = document.getElementById('inside-sidebar');
var toggle_button = document.getElementById('expand-list');
function toggle_list() {
    if (inside_sidebar.className === 'visible') {
        inside_sidebar.className = 'invisible';
		toggle_button.innerHTML = "<span class=\"nav-button\">Show</span>"
    } else {
        inside_sidebar.className = 'visible';
		toggle_button.innerHTML = "<span class=\"nav-button\">Hide</span>"
    }
}
toggle_button.addEventListener('click', toggle_list);

var dark_mode = window.matchMedia('(prefers-color-scheme: dark)').matches;
var body = document.getElementById('body');
var sidebar = document.getElementById('sidebar');
var md_body = document.getElementById('markdown-body');
var dark_mode_button = document.getElementById('toggle-dark-mode');

if (dark_mode) {
        body.className = "dark-mode-on";
        sidebar.className = "sidebar-dark";
        md_body.className = "markdown-body-dark";
        dark_mode_button.innerHTML = "<span class=\"nav-button\">🌃 Turn off dark mode</span>";
}

function toggle_dark_mode() {
    if (dark_mode) {
        body.className = "dark-mode-off";
        sidebar.className = "sidebar";
        md_body.className = "markdown-body";
        dark_mode = false;
        dark_mode_button.innerHTML = "<span class=\"nav-button\">🏙 Turn on dark mode</span>"
    } else {
        body.className = "dark-mode-on";
        sidebar.className = "sidebar-dark";
        md_body.className = "markdown-body-dark";
        dark_mode = true;
        dark_mode_button.innerHTML = "<span class=\"nav-button\">🌃 Turn off dark mode</span>"
    }
}

dark_mode_button.addEventListener('click', toggle_dark_mode);
