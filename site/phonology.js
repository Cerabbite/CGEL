const getLanguages = async () => {


const parent = document.querySelector('#languages');


const languages = await fetch('sample.txt').then(x => x.text()).then((data) => data.split(',').sort());

If (languages) {


    languages.forEach((language) => {


 const option = document.createElement('option');


option.value = language;


 option.text = language;


       parent.appendChild(option);

    })
}

}