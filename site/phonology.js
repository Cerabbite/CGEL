const getLanguages = async () => {


const parent = document.querySelector('#languages');


const languages = await fetch('languages.txt').then(x => x.text()).then((data) => data.split(/\r?\n/).sort());

If (languages) {


    languages.forEach((language) => {


 const option = document.createElement('option');


option.value = language;


 option.text = language;


       parent.appendChild(option);

    })
}

}
