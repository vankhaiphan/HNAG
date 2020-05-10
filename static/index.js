document.addEventListener('DOMContentLoaded', () => {
    const request = new XMLHttpRequest();
    request.open('GET', '/load');

    request.onload = () => {        
        const data = JSON.parse(request.responseText);

        if (data.success) {
            const lname = `${data.name}`
            const lrating = `${data.rating}`

            const card = document.createElement("div class='card'")                            
        }
        else {                        
        }
    }

    request.send();
});