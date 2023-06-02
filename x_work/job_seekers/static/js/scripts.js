new Autocomplete('#autocomplete',{
search : input => {
    console.log(input)
    const url = `/get_city/?search=${input}`
    return new Promise(resolve => {
        fetch(url)
        .then(response=>response.json())
        .then(data =>{
            console.log(data.payload)
            resolve(data.payload)
        })
    })
},

renderResult : (result, props)=>{
    console.log(props)
    let group=''
    if(result % 3 == 0){
        group=`<li class="group">Group</li>`
    }
    const listItem = document.createElement('li');
    listItem.innerHTML = `
        ${group}
        <div class="wiki-title">
            ${result.state} / ${result.city}
        </div>
    `;
    listItem.addEventListener('click', () => {
        const input = document.querySelector('#autocomplete input');
        input.value = result.city;
        const hidden_input=document.querySelector('#autocomplete #city_id')
        hidden_input.value = result.id
        closeAutocomplete(); // Закрыть список автодополнения
    });
    listItem.addEventListener('mouseenter', () => {
        listItem.classList.add('highlight');
    });
    listItem.addEventListener('mouseleave', () => {
        listItem.classList.remove('highlight');
    });
    
    return listItem;
}
});

function closeAutocomplete() {
const list = document.querySelector('#autocomplete').querySelector('ul');
list.classList.remove('autocomplete-result-list'); // Скрыть список автодополнения
}
