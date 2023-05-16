const container = document.getElementsByClassName('container_content')[0]


function search_voice_in_anime(){
    const inputTextTitle = document.getElementById('inputField').value;
    const inputTextVoice = document.getElementById('voice').value;
    container.innerHTML = '';
    $.get("/voice", {inputTextTitle: inputTextTitle, inputTextVoice: inputTextVoice}, function(response) {
        for (let i = 0; i < response.length; i++) {
            if (typeof response[i] === 'string'){
                container.innerHTML = response[i];
            }else{
                let sait = response[i][0];
                let title = response[i][1].charAt(0) + response[i][1].slice(1).toLowerCase();
                let href = response[i][4];
                let img;
                if (sait === 'YUMMYANIME.TV'){
                    img = 'static/img/yummyanime.png';
                } else if (sait === 'ANIMEVOST'){
                    img = 'static/img/animevost.png';
                }else if (sait === 'AMEDIA_ONLINE'){
                    img = 'static/img/amedia_onlain.png';
                }else if (sait === 'ANIDUB.VIP'){
                    img = 'static/img/anidub_vip.png';
                }else{
                     img = 'static/img/jut_su.png';
                }

                const cardLinkElement = document.createElement('a');
                cardLinkElement.href = href;
                cardLinkElement.classList.add('card-link');

                const cardTitleElement = document.createElement('h2');
                cardTitleElement.textContent = title;
                cardLinkElement.appendChild(cardTitleElement);

                const cardImageElement = document.createElement('img');
                cardImageElement.src = img;
                cardImageElement.alt = title; // Добавим описание изображения
                cardLinkElement.appendChild(cardImageElement);

                container.appendChild(cardLinkElement);
            }
        }
    });
}


function search_series_in_anime(){
    const inputTextTitle = document.getElementById('inputField').value;
    const inputTextSeries = document.getElementById('spinbox').value;
    container.innerHTML = '';
    $.get("/series", {inputTextTitle: inputTextTitle, inputTextSeries: inputTextSeries}, function(response) {
        for (let i = 0; i < response.length; i++) {
            if (typeof response[i] === 'string'){
                container.innerHTML = response[i];
            }else{
                let sait = response[i][0];
                let title = response[i][1].charAt(0) + response[i][1].slice(1).toLowerCase();
                let href = response[i][4];
                let img;
                if (sait === 'YUMMYANIME.TV'){
                    img = 'static/img/yummyanime.png';
                } else if (sait === 'ANIMEVOST'){
                    img = 'static/img/animevost.png';
                }else if (sait === 'AMEDIA_ONLINE'){
                    img = 'static/img/amedia_onlain.png';
                }else if (sait === 'ANIDUB.VIP'){
                    img = 'static/img/anidub_vip.png';
                }else{
                     img = 'static/img/jut_su.png';
                }

                const cardLinkElement = document.createElement('a');
                cardLinkElement.href = href;
                cardLinkElement.classList.add('card-link');

                const cardTitleElement = document.createElement('h2');
                cardTitleElement.textContent = title;
                cardLinkElement.appendChild(cardTitleElement);

                const cardImageElement = document.createElement('img');
                cardImageElement.src = img;
                cardImageElement.alt = title; // Добавим описание изображения
                cardLinkElement.appendChild(cardImageElement);

                container.appendChild(cardLinkElement);
            }
        }
    });
}