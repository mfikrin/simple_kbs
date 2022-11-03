const submit = document.getElementById("submit-button");

submit.addEventListener("click", (e) => {
  e.preventDefault();
  const data = {
    SAT: parseFloat(document.getElementById("SAT").value),
    SATSP: parseFloat(document.getElementById("SATSP").value),
    OAT: parseFloat(document.getElementById("OAT").value),
    MAT: parseFloat(document.getElementById("MAT").value),
    RAT: parseFloat(document.getElementById("RAT").value),
    SAFS: parseFloat(document.getElementById("SAFS").value),
    RAFS: parseFloat(document.getElementById("RAFS").value),
    SAFSCS: parseFloat(document.getElementById("SAFSCS").value),
    RAFSCS: parseFloat(document.getElementById("RAFSCS").value),
    OADCS: parseFloat(document.getElementById("OADCS").value),
    RADCS: parseFloat(document.getElementById("RADCS").value),
    CCVCS: parseFloat(document.getElementById("CCVCS").value),
    HCVCS: parseFloat(document.getElementById("HCVCS").value),
    SADSPSP: parseFloat(document.getElementById("SADSPSP").value),
    SADSP: parseFloat(document.getElementById("SADSP").value),
    OMI: parseFloat(document.getElementById("OMI").value),
  };
  console.log(data);

  fetch("https://simple-kbs.herokuapp.com/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      document.getElementById("result").innerHTML = "Result | Fault Detection Ground Truth : " + data["Fault Detection Ground Truth"];
      let outputSection = document.getElementById("output-section");
      outputSection.style.display = "block";
      window.scrollTo(0, 0);
    })
    .catch((error) => {
      console.error("Error:", error);
      document.getElementById("result").innerHTML = "Error";
      let outputSection = document.getElementById("output-section");
      outputSection.style.display = "block";
      window.scrollTo(0, 0);
    })
 
});

// form.addEventListener('submit', (e) => {
//     e.preventDefault();
//     const data = {
//         "SAT" : form.elements["SAT"].value,
//         // "SATSP" : 0,
//         // "OAT" : 0,
//         // "MAT" :0,
//         // "RAT":0,
//         // "SAFS":0,
//         // "RAFS":0,
//         // "SAFSCS":0,
//         // "RAFSCS":0,
//         // "OADCS":0,
//         // "RADCS":0,
//         // "CCVCS":0,
//         // "HCVCS":0,
//         // "SADSPSP":0,
//         // "SADSP":0,
//         // "OMI":0
//     }
//     console.log(data);

//     });

let helpButton = document.getElementById("help-btn");
let helpPopup = document.getElementById("help-section");
let helpClose = document.getElementById("help-close");

helpButton.addEventListener("click", function () {
  helpPopup.style.display = "block";
});
helpClose.addEventListener("click", function (e) {
  helpPopup.style.display = "none";
});

let outputSection = document.getElementById("output-section");
let outputClose = document.getElementById("output-close");
outputClose.addEventListener("click", function (e) {
    outputSection.style.display = "none";
});