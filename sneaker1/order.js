let arr = [];
let search  = document.getElementById("search");
let a  = "";
let index = document.getElementById("index")
let text = document.getElementsByClassName("TextBox")
let text1 = document.getElementsByClassName("TextBox1")
let text2 = document.getElementsByClassName("TextBox2")
let text3 = document.getElementsByClassName("TextBox3")

axios.post('https://countriesnow.space/api/v0.1/countries/cities', {
        country: "Kazakhstan"
}).then(res => {
        for(let i=0; i<res.data.data.length; i++){
            arr[i]=res.data.data[i];
          }
})


let res = document.getElementById("result");
let checker = true;

function showCity() {
  let fiteredCities = arr.filter(item => 
    item.includes(search.value));
    
    res.innerHTML = '';
    let list = '';
    for (i=0; i<fiteredCities.length; i++) {
      list += '<option onclick="replaceValue(this)">' + fiteredCities[i] + '</option>';
    }
    res.innerHTML = '<ul>' + list + '</ul>';
    console.log(search === document.activeElement);
    if(search === document.activeElement){
      res.style.display="block";
  }
}


 function replaceValue(item) {
  search.value=item.innerText;
  a=item.innerText;
  res.style.display="none";
}


function zakazOrd(){
let cnt=0;
for(let i=0; i<text.length; i++){
    if(text[i].value===""){
        cnt++;
    }
}


for(let i=0; i<text1.length; i++){
    if(!text1[i].checked){
        cnt++;
    }
}

for(let i=0; i<text2.length; i++){
    if(!text2[i].checked){
        cnt++;
    }
}

for(let i=0; i<text3.length; i++){
    if(!text3[i].checked){
        cnt++;
    }
}

if(search.value===""){
    cnt++;
}
if(index.value===""){
    cnt++;
}

console.log(cnt)
if(cnt===4){
    alert("Zakaz is ordered")
}else if(cnt<4){
    alert("You should tick one of the checkbox in each input")
}else{
    alert('All field must be filled');
}

}

