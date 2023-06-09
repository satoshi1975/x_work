// new Autocomplete('#autocomplete',{
//     search : input => {
//         console.log(input)
//         const url = `/get_city/?search=${input}`
//         return new Promise(resolve => {
//             fetch(url)
//             .then(response=>response.json())
//             .then(data =>{
//                 console.log(data.payload)
//                 resolve(data.payload)
//             })
//         })
//     },
    
//     renderResult : (result, props)=>{
//         console.log(props)
//         let group=''
//         if(result % 3 == 0){
//             group=`<li class="group">Group</li>`
//         }
//         const listItem = document.createElement('li');
//         listItem.innerHTML = `
//             ${group}
//             <div class="wiki-title">
//                 ${result.state} / ${result.city}
//             </div>
//         `;
//         listItem.addEventListener('click', () => {
//             const input = document.querySelector('#autocomplete input');
//             input.value = result.city;
//             const hidden_input=document.querySelector('#autocomplete #city_id')
//             hidden_input.value = result.id
//             closeAutocomplete(); // Закрыть список автодополнения
//         });
//         listItem.addEventListener('mouseenter', () => {
//             listItem.classList.add('highlight');
//         });
//         listItem.addEventListener('mouseleave', () => {
//             listItem.classList.remove('highlight');
//         });
        
//         return listItem;
//     }
//     });
    
//     function closeAutocomplete() {
//     const list = document.querySelector('#autocomplete').querySelector('ul');
//     list.classList.remove('autocomplete-result-list'); // Скрыть список автодополнения
//     }
    
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

    // 
    
    
    
    function removeEmptyFields() {
        var form = document.getElementById("search-form-vacancy");
        var inputs = form.getElementsByTagName("input");
        var selects = form.getElementsByTagName("select");
    
        // Remove empty values from input fields
        for (var i = 0; i < inputs.length; i++) {
          var input = inputs[i];
          if (input.value.trim() === "" || input.value === "false" || input.value === "None") {
            input.remove();
          }
        }
    
        // Remove empty values from select fields
        for (var i = 0; i < selects.length; i++) {
          var select = selects[i];
          var selectedOption = select.options[select.selectedIndex];
          if (selectedOption.value === "false" || selectedOption.value === "None") {
            select.remove();
          }
        }
      }
    
      // Attach the removeEmptyFields function to the form's submit event
      var form = document.getElementById("search-form-vacancy");
      form.addEventListener("submit", removeEmptyFields);