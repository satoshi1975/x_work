
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

window.addEventListener('DOMContentLoaded', (event) => {
    const addFieldsButton = document.getElementById('addFieldsButton');
    const inputFieldsContainer = document.getElementById('inputFieldsContainer');
  
    let fieldCounter = 0;
  
    addFieldsButton.addEventListener('click', (event) => {
      event.preventDefault(); // Предотвращаем отправку формы
  
      if (fieldCounter < 2 || (fieldCounter >= 2 && arePreviousFieldsFilled())) {
        fieldCounter++;
        const fieldsWrapper = document.createElement('div');
        fieldsWrapper.classList.add('fields-wrapper');
  
        const educationalInstitutionInput = document.createElement('input');
        educationalInstitutionInput.type = 'text';
        educationalInstitutionInput.name='institution'
        educationalInstitutionInput.placeholder = 'Учебное заведение';
  
        const startDateInput = document.createElement('input');
        startDateInput.type = "date" ;
        startDateInput.name='study_start'
        startDateInput.placeholder = 'Начало обучения';
  
        const endDateInput = document.createElement('input');
        endDateInput.type = "date" ;
        endDateInput.name='study_end'
        endDateInput.placeholder = 'Конец обучения';
        endDateInput.style='padding-top: 10px;'
  
        fieldsWrapper.appendChild(educationalInstitutionInput);
        fieldsWrapper.appendChild(startDateInput);
        fieldsWrapper.appendChild(endDateInput);
        inputFieldsContainer.appendChild(fieldsWrapper);
      }
    });
  
    function arePreviousFieldsFilled() {
      const previousFields = Array.from(inputFieldsContainer.getElementsByClassName('fields-wrapper'));
      const lastFieldsWrapper = previousFields[previousFields.length - 1];
      const educationalInstitutionInput = lastFieldsWrapper.querySelector('input:nth-child(1)');
      const startDateInput = lastFieldsWrapper.querySelector('input:nth-child(2)');
      const endDateInput = lastFieldsWrapper.querySelector('input:nth-child(3)');
      
      return educationalInstitutionInput.value !== '' && startDateInput.value !== '' && endDateInput.value !== '';
    }
  });
  


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







function closeAutocomplete() {
const occupationList = document.querySelector('#occupation-list');
occupationList.innerHTML = '';
}

// Функция для обработки выбора профессии из списка
function handleSelection(occupation) {
const occupationInput = document.querySelector('#occupation-input');
occupationInput.value = occupation;
closeAutocomplete();
}

// Обработчик ввода в поле автодополнения
function handleInput() {
const input = document.querySelector('#occupation-input').value;
const url = `/get_occupation/?search=${input}`;

fetch(url)
    .then(response => response.json())
    .then(data => {
    const occupationList = document.querySelector('#occupation-list');
    occupationList.innerHTML = '';

    if (data.status) {
        const payload = data.payload;
        payload.forEach(occupation => {
        const listItem = document.createElement('li');
        listItem.textContent = occupation.occupation;
        listItem.addEventListener('click', () => handleSelection(occupation.occupation));
        occupationList.appendChild(listItem);
        });
    }
    })
    .catch(error => {
    console.log('Произошла ошибка:', error);
    });
}

// Добавление обработчика события ввода в поле автодополнения
const occupationInput = document.querySelector('#occupation-input');
occupationInput.addEventListener('input', handleInput);




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



  function addWorkExperienceFields() {
    var workExperienceFields = document.getElementById('work-experience-fields');

    // Проверка, что все предыдущие поля заполнены
    var previousFields = workExperienceFields.querySelectorAll('input');
    var isPreviousFieldsFilled = true;
    previousFields.forEach(function(field) {
        if (field.value.trim() === '') {
            isPreviousFieldsFilled = false;
        }
    });

    if (isPreviousFieldsFilled) {
        // Создание новых полей "компания", "должность", "начало работы" и "конец работы"
        var companyInput = document.createElement('input');
        companyInput.type = 'text';
        companyInput.name = 'company';
        companyInput.placeholder = 'Компания';

        var positionInput = document.createElement('input');
        positionInput.type = 'text';
        positionInput.name = 'position';
        positionInput.placeholder = 'Должность';

        var startDateInput = document.createElement('input');
        startDateInput.type = 'date';
        startDateInput.name = 'work_start';
        startDateInput.placeholder = 'Начало работы';

        var endDateInput = document.createElement('input');
        endDateInput.type = 'date';
        endDateInput.name = 'work_end';
        endDateInput.placeholder = 'Конец работы';

        var closeButton = document.createElement('button');
        closeButton.classList.add('close-button');
        closeButton.innerText = 'Закрыть';
        closeButton.addEventListener('click', () => {
            var fieldset = companyInput.parentNode;
            fieldset.remove();
        });

        var fieldset = document.createElement('fieldset');
        fieldset.appendChild(companyInput);
        fieldset.appendChild(positionInput);
        fieldset.appendChild(startDateInput);
        fieldset.appendChild(endDateInput);
        fieldset.appendChild(closeButton);

        workExperienceFields.appendChild(fieldset);
    }
}



window.addEventListener('DOMContentLoaded', (event) => {
    const addFieldsButton = document.getElementById('addFieldsButton');
    const inputFieldsContainer = document.getElementById('inputFieldsContainer');

    let fieldCounter = 0;

    addFieldsButton.addEventListener('click', (event) => {
        event.preventDefault(); // Предотвращаем отправку формы

        if (fieldCounter < 2 || (fieldCounter >= 2 && arePreviousFieldsFilled())) {
            fieldCounter++;
            const fieldsWrapper = document.createElement('div');
            fieldsWrapper.classList.add('fields-wrapper');

            const educationalInstitutionInput = document.createElement('input');
            educationalInstitutionInput.type = 'text';
            educationalInstitutionInput.name = 'institution';
            educationalInstitutionInput.placeholder = 'Учебное заведение';

            const startDateInput = document.createElement('input');
            startDateInput.type = "date";
            startDateInput.name = 'study_start';
            startDateInput.placeholder = 'Начало обучения';

            const endDateInput = document.createElement('input');
            endDateInput.type = "date";
            endDateInput.name = 'study_end';
            endDateInput.placeholder = 'Конец обучения';
            endDateInput.style = 'padding-top: 10px;';

            const closeButton = document.createElement('button');
            closeButton.classList.add('close-button');
            closeButton.innerText = 'Закрыть';
            closeButton.addEventListener('click', () => {
                fieldsWrapper.remove();
                fieldCounter--; // Уменьшаем счетчик полей после удаления
            });

            fieldsWrapper.appendChild(educationalInstitutionInput);
            fieldsWrapper.appendChild(startDateInput);
            fieldsWrapper.appendChild(endDateInput);
            fieldsWrapper.appendChild(closeButton);
            inputFieldsContainer.appendChild(fieldsWrapper);
        }
    });

    function arePreviousFieldsFilled() {
        const previousFields = Array.from(inputFieldsContainer.getElementsByClassName('fields-wrapper'));
        const lastFieldsWrapper = previousFields[previousFields.length - 1];
        const educationalInstitutionInput = lastFieldsWrapper.querySelector('input:nth-child(1)');
        const startDateInput = lastFieldsWrapper.querySelector('input:nth-child(2)');
        const endDateInput = lastFieldsWrapper.querySelector('input:nth-child(3)');

        return educationalInstitutionInput.value !== '' && startDateInput.value !== '' && endDateInput.value !== '';
    }
});
// window.onload = function() {
// document.getElementById('search-form-vacancy').addEventListener('submit', function(event) {
//     var form = event.target;
//     var elements = form.elements;

//     for (var i = 0; i < elements.length; i++) {
//     var element = elements[i];
    
//     if (element.tagName === 'SELECT') {
//         if (element.value === 'false') {
//         form.removeChild(element);
//         }
//     } else if (element.tagName === 'INPUT' && element.value === '') {
//         form.removeChild(element);
//     }
//     }
// });
// };



// document.getElementById("search-form-vacancy").addEventListener("submit", function(event) {
//     var form = event.target;
//     var inputs = form.querySelectorAll("input[type=text], select");

//     for (var i = 0; i < inputs.length; i++) {
//         var input = inputs[i];

//         if (input.value.trim() === "" || input.value === "false") {
//             input.disabled = true;
//         }
//     }
// });
