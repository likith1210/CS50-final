document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#add').addEventListener('click', () => {

        med=document.querySelector('#med').value;
        qty=document.querySelector('#qty').value;
        console.log(med);
        fetch('/med', {
            method: 'POST',
            body: JSON.stringify({
                medicine: med,
                quantity: qty,
            })
        })
        .then(response => response.json())  

        myhtml=`<input type="text" value="${med}" class="inner_text" readonly>
        <input type="text" value="${qty}" class="inner_text" readonly>`

        document.querySelector("#dynamic").innerHTML += myhtml

        document.querySelector('#med').value=""
        document.querySelector('#qty').value=""

        return false
    })
})