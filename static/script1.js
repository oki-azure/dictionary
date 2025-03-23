function searchWord() {
    let word = document.getElementById("searchWord").value.trim();
    if (!word) {
        alert("Please enter a word!");
        return;
    }
    
    fetch(`/search/${word}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = `Meaning: ${data.meaning}`;
        })
        .catch(error => console.error("Error:", error));
}

function addWord() {
    let word = document.getElementById("newWord").value.trim();
    let meaning = document.getElementById("newMeaning").value.trim();

    if (!word || !meaning) {
        alert("Please enter both word and meaning!");
        return;
    }

    fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ word: word, meaning: meaning })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("addResult").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
}

function updateWord() {
    let word = document.getElementById("updateWord").value.trim();
    let newMeaning = document.getElementById("updateMeaning").value.trim();

    if (!word || !newMeaning) {
        alert("Please enter both word and new meaning!");
        return;
    }

    fetch("/update", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ word: word, new_meaning: newMeaning })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("updateResult").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
}


function deleteWord() {
    let word = document.getElementById("deleteWord").value.trim();
    if (!word) {
        alert("Please enter a word to delete!");
        return;
    }

    fetch(`/delete/${word}`, { method: "DELETE" })
        .then(response => response.json())
        .then(data => {
            document.getElementById("deleteResult").innerText = data.message;
        })
        .catch(error => console.error("Error:", error));
}

function getSuggestions() {
    let prefix = document.getElementById("searchWord").value.trim();
    if (prefix.length < 1) {
        document.getElementById("suggestions").innerHTML = "";
        return;
    }

    fetch(`/suggest/${prefix}`)
        .then(response => response.json())
        .then(data => {
            let suggestionsBox = document.getElementById("suggestions");
            suggestionsBox.innerHTML = "";
            data.suggestions.forEach(word => {
                let div = document.createElement("div");
                div.innerText = word;
                div.onclick = () => {
                    document.getElementById("searchWord").value = word;
                    searchWord();
                };
                suggestionsBox.appendChild(div);
            });
        })
        .catch(error => console.error("Error:", error));
}

function fetchAllWords() {
    fetch('/words')
        .then(response => response.json())
        .then(data => {
            const wordListDiv = document.getElementById('wordList');
            wordListDiv.innerHTML = ''; // Clear previous content

            data.forEach(([word, meaning]) => {
                wordListDiv.innerHTML += `<div class="word-entry">
                    <strong>${word}</strong><br>
                    <em>${meaning}</em>
                </div>`;
            });
        })
        .catch(error => console.error('Error fetching words:', error));
}



$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {

        if (this.hash !== "") {

            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        } 
    });
});

function scrollToSection(sectionId) {
    var section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
  }

$('#nav-toggle').click(function(){
    $(this).toggleClass('is-active')
    $('ul.nav').toggleClass('show');
});