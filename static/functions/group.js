let add_participant_button = document.getElementById("show-add-participant-button");
add_participant_button.addEventListener("click", function() {
    let add_participant_div = document.getElementById("add-participant-div");
    console.log(add_participant_div);
    add_participant_div.style.display = add_participant_div.style.display != "block" ? "block" : "none";
});

let edit_participant_buttons = document.getElementsByName("show-edit-participant-button");

for (const edit_participant_button of edit_participant_buttons){
  edit_participant_button.addEventListener("click", function() {
      let edit_participant_div = edit_participant_button.parentElement.children[1];
      edit_participant_div.style.display = edit_participant_div.style.display != "block" ? "block" : "none";
      edit_participant_button.value = edit_participant_button.value == "Edit Participant" ? "Cancel" : "Edit Participant";
      edit_participant_button.innerHTML = edit_participant_button.innerHTML == "Edit Participant" ? "Cancel" : "Edit Participant";
  });
}