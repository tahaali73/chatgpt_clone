
async function postData(url="",data={}) {
    const responce = await fetch(url, {
        method: "POST", headers: {
            "Content-Type": "application/json",
        }, body: JSON.stringify(data),
    });
    return responce.json();
    
}

sendButton.addEventListener("click", async()=>{
    questionInput = document.getElementById("questionInput").value;
    document.getElementById("questionInput").value="";
    document.querySelector(".right2.flex-1.flex.flex-col.overflow-hidden").style.display = "block"
    document.querySelector(".right1.flex-1.flex.flex-col.overflow-hidden").style.display = "none"

    question2.innerHTML = questionInput;
    
    let result = await postData("/api",{"question":questionInput})
    solution.innerHTML = result.result
})