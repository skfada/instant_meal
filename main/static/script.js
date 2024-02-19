// Set current year
const yearEl = document.querySelector(".year");
const currentYear = new Date().getFullYear();
yearEl.textContent = currentYear;
///////////////////////////////////////////////////////////
// Make mobile navigation work

const btnNavEl = document.querySelector(".btn-mobile-nav");
const headerEl = document.querySelector(".header");

btnNavEl.addEventListener("click", function () {
  headerEl.classList.toggle("nav-open");
});

///////////////////////////////////////////////////////////
// Smooth scrolling animation

// const allLinks = document.querySelectorAll("a:link");

// allLinks.forEach(function (link) {
//   link.addEventListener("click", function (e) {
//     e.preventDefault();
//     const href = link.getAttribute("href");

//     // Scroll back to top
//     if (href === "#")
//       window.scrollTo({
//         top: 0,
//         behavior: "smooth",
//       });

//     // Scroll to other links

//     // Close mobile naviagtion
//     if (link.classList.contains("main-nav-link"))
//       headerEl.classList.toggle("nav-open");
//   });
// });

///////////////////////////////////////////////////////////
// Sticky navigation

const sectionHeroEl = document.querySelector(".section-hero");

const obs = new IntersectionObserver(
  function (entries) {
    const ent = entries[0];
    console.log(ent);

    if (ent.isIntersecting === false) {
      document.body.classList.add("sticky");
    }

    if (ent.isIntersecting === true) {
      document.body.classList.remove("sticky");
    }
  },
  {
    // In the viewport
    root: null,
    threshold: 0,
    rootMargin: "-80px",
  }
);
obs.observe(sectionHeroEl);

///////////////////////////////////////////////////////////
// Fixing flexbox gap property missing in some Safari versions
function checkFlexGap() {
  var flex = document.createElement("div");
  flex.style.display = "flex";
  flex.style.flexDirection = "column";
  flex.style.rowGap = "1px";

  flex.appendChild(document.createElement("div"));
  flex.appendChild(document.createElement("div"));

  document.body.appendChild(flex);
  var isSupported = flex.scrollHeight === 1;
  flex.parentNode.removeChild(flex);
  console.log(isSupported);

  if (!isSupported) document.body.classList.add("no-flexbox-gap");
}
checkFlexGap();

///////////////////////////////////////////////////////////
// Password visibility toggle
function togglePasswordVisibility() {
  const passwordInput = document.getElementById("login_pwd2");
  const toggleElement = document.querySelector(".password-toggler");

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    toggleElement.textContent = "Hide"; // Update toggle text
  } else {
    passwordInput.type = "password";
    toggleElement.textContent = "Show"; // Update toggle text
  }
}

///////////////////////////////////////////////////////////
// Register visibility toggle (password1)
function togglePasswordVisibility() {
  const passwordInput = document.getElementById("reg_pwd1");
  const toggleElement = document.querySelector(".password-toggler");

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    toggleElement.textContent = "Hide"; // Update toggle text
  } else {
    passwordInput.type = "password";
    toggleElement.textContent = "Show"; // Update toggle text
  }
}

///////////////////////////////////////////////////////////
// Register visibility toggle (password2)
function togglePasswordVisibility_2() {
  const passwordInput = document.getElementById("reg_pwd2");
  const toggleElement = document.querySelector(".password-toggler_2");

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    toggleElement.textContent = "Hide"; // Update toggle text
  } else {
    passwordInput.type = "password";
    toggleElement.textContent = "Show"; // Update toggle text
  }
}

///////////////////////////////////////////////////////////
// Register visibility toggle (password1)
function togglePasswordVisibility_3() {
  const passwordInput = document.getElementById("login_pwd2");
  const toggleElement = document.querySelector(".password-toggler");

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    toggleElement.textContent = "Hide"; // Update toggle text
  } else {
    passwordInput.type = "password";
    toggleElement.textContent = "Show"; // Update toggle text
  }
}

///////////////////////////////////////////////////////////
// Form validation for registration page
// Valited password
// function checkPassword() {
//   var password = document.getElementById("reg_pwd1").value;
//   var confirmPassword = document.getElementById("reg_pwd2").value;

//   if (password !== confirmPassword) {
//     alert("Passwords do not match");
//     return false;
//   }
//   return true;
// }

function checkPassword() {
  var password = document.getElementById("reg_pwd1").value;
  var confirmPassword = document.getElementById("reg_pwd2").value;
  var passwordError = document.getElementById("passwordError"); // Get the error message element

  if (password !== confirmPassword) {
    passwordError.textContent = "Passwords do not match."; // Update the error message
    return false;
  } else {
    passwordError.textContent = ""; // Clear the error message if passwords match
  }
  return true;
}

// ///////////////////////////////////////////////////////////
// // Redirect to User Register page
// function regLink() {
//   window.location.href = "/main/templates/user/register.html";
// }
// // Redirect to User login page
// function LoginLink() {
//   window.location.href = "/main/templates/user/login.html";
// }
// // Redirect to User login page
// function LoginLink() {
//   window.location.href = " /main/templates/seller/login.html";
// }
// // Redirect to User Register page
// function regLink() {
//   window.location.href = "/main/templates/seller/register.html";
// }

///////////////////////////////////////////////////////////
// Dropdown menu functionality
function toggleDropdown() {
  var dropdown = document.getElementById("myDropdown");
  dropdown.classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches(".dropbtn")) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};
// https://unpkg.com/smoothscroll-polyfill@0.4.4/dist/smoothscroll.min.js

/*
.no-flexbox-gap .main-nav-list li:not(:last-child) {
  margin-right: 4.8rem;
}

.no-flexbox-gap .list-item:not(:last-child) {
  margin-bottom: 1.6rem;
}

.no-flexbox-gap .list-icon:not(:last-child) {
  margin-right: 1.6rem;
}

.no-flexbox-gap .delivered-faces {
  margin-right: 1.6rem;
}

.no-flexbox-gap .meal-attribute:not(:last-child) {
  margin-bottom: 2rem;
}

.no-flexbox-gap .meal-icon {
  margin-right: 1.6rem;
}

.no-flexbox-gap .footer-row div:not(:last-child) {
  margin-right: 6.4rem;
}

.no-flexbox-gap .social-links li:not(:last-child) {
  margin-right: 2.4rem;
}

.no-flexbox-gap .footer-nav li:not(:last-child) {
  margin-bottom: 2.4rem;
}

@media (max-width: 75em) {
  .no-flexbox-gap .main-nav-list li:not(:last-child) {
    margin-right: 3.2rem;
  }
}

@media (max-width: 59em) {
  .no-flexbox-gap .main-nav-list li:not(:last-child) {
    margin-right: 0;
    margin-bottom: 4.8rem;
  }
}
*/
