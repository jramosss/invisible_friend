let add_participant_button = document.getElementById("show-add-participant-button");

add_participant_button.addEventListener("click", function() {
    let div = document.getElementById("add-participant-div");
    div.style.display = div.style.display != "block" ? "block" : "none";
    add_participant_button.value = add_participant_button.value == "Add Participant" ? "Cancel" : "Add Participant";
});

let edit_participant_buttons = document.getElementsByName("show-edit-participant-button");

for (const edit_participant_button of edit_participant_buttons){
  edit_participant_button.addEventListener("click", function() {
      let div = edit_participant_button.parentElement.children[1];
      div.style.display = div.style.display != "block" ? "block" : "none";
      edit_participant_button.value = edit_participant_button.value == "Edit Participant" ? "Cancel" : "Edit Participant";
      edit_participant_button.innerHTML = edit_participant_button.innerHTML == "Edit Participant" ? "Cancel" : "Edit Participant";
  });
}