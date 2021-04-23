$(document).ready(function () {

  // Get the form.
  var form = $("#entry-form");

  // console.log(form);

  // Get the messages div.
  var formMessages = $("#gate-response");
  //console.log(formMessages);

  // Set up an event listener for the contact form.
  form.submit(function (event) {
    // Stop the browser from submitting the form.
    event.preventDefault();
    console.log("prevent_submit");

    // Serialize the form data.
    var formData = $(form).serialize();

    // Submit the form using AJAX.
    $.ajax({
      type: "POST",
      url: $(form).attr("action"),
      data: formData,
    })

      .done(function (response) {
        // Make sure that the formMessages div has the 'success' class.
        $(formMessages).removeClass("error");
        $(formMessages).addClass("success");

        // Set the message text.
        $(formMessages).append(response);

        // Clear the form.
        $("#name").val("");
        $("#email").val("");
        $("#message").val("");
      })

      .fail(function (data) {
        // Make sure that the formMessages div has the 'error' class.
        $(formMessages).removeClass("success");
        $(formMessages).addClass("error");

        // Set the message text.
        if (data.responseText !== "") {
          $(formMessages).append(data);
        } else {
          $(formMessages).append("Oops! Something went wrong...");
        }
      });
  });
});

// Camera capture
(function () {
  var width = 320; // We will scale the photo width to this
  var height = 0; // This will be computed based on the input stream

  var streaming = false;

  var video = null;
  var canvas = null;
  var photo = null;
  var startbutton = null;

  function startup() {
    video = document.getElementById("videoElement");
    canvas = document.getElementById("canvas");
    photo = document.getElementById("photo");
    startbutton = document.getElementById("startbutton");
    picture = document.getElementById("custId"); // delete soon
    navigator.mediaDevices
      .getUserMedia({
        video: true,
        audio: false,
      })
      .then(function (stream) {
        video.srcObject = stream;
        video.play();
      })
      .catch(function (err) {
        console.log("An error occurred: " + err);
      });

    video.addEventListener(
      "canplay",
      function (ev) {
        if (!streaming) {
          height = video.videoHeight / (video.videoWidth / width);

          if (isNaN(height)) {
            height = width / (4 / 3);
          }

          video.setAttribute("width", width);
          video.setAttribute("height", height);
          canvas.setAttribute("width", width);
          canvas.setAttribute("height", height);
          streaming = true;
        }
      },
      false
    );

    startbutton.addEventListener(
      "click",
      function (ev) {
        takepicture();
        ev.preventDefault();
      },
      false
    );

    clearphoto();
  }

  function clearphoto() {
    var context = canvas.getContext("2d");
    context.fillStyle = "#AAA";
    context.fillRect(0, 0, canvas.width, canvas.height);

    var data = canvas.toDataURL("image/png");
    photo.setAttribute("src", data);
  }

  function takepicture() {
    var context = canvas.getContext("2d");
    if (width && height) {
      canvas.width = width;
      canvas.height = height;
      context.drawImage(video, 0, 0, width, height);

      var data = canvas.toDataURL("image/png");
      picture.value = data; // set image input url to data url
      //console.log(data);
      photo.setAttribute("src", data);
    } else {
      clearphoto();
    }
  }

  window.addEventListener("load", startup, false);
})();
