async function get_group() {
    fetch("{% url 'groups_all' %", {cache: "no-store"})
    .then((res) => res.json())
    .then((rows) => {
        for (let i = 0; i < rows.langth; i++) {
            line = rows[i]
            document.getElementById('groups').innerHTML +=
            "<p>"+line[0] + "<br/>;" + line[1] + "</p>\n";
        }
        setTimeout('get_group()', 4000);
    })
    .catch((error) => {
        alert(error);
    });
}

