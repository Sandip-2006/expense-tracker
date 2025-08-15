document.addEventListener("DOMContentLoaded",()=>{
    const deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach((btn) => {
        btn.addEventListener("click",(e)=>{
            const confirmed = confirm("Are you sure you want to delete this expense?")

            if(!confirmed){
                e.preventDefault();
            }
        })
    });
})