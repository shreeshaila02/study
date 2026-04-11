// Switch between forms
function showRegister() {
  document.getElementById("loginForm").classList.add("hidden");
  document.getElementById("registerForm").classList.remove("hidden");
}

function showLogin() {
  document.getElementById("registerForm").classList.add("hidden");
  document.getElementById("loginForm").classList.remove("hidden");
}

// Register functionality
function register() {
  const username = document.getElementById("registerUsername").value;
  const email = document.getElementById("registerEmail").value;
  const password = document.getElementById("registerPassword").value;
  const confirm = document.getElementById("registerConfirm").value;

  if (!username || !email || !password || !confirm) {
    alert("Please fill in all fields.");
    return;
  }

  if (password !== confirm) {
    alert("Passwords do not match.");
    return;
  }

  // Store user in localStorage (demo only)
  localStorage.setItem(username, JSON.stringify({ email, password }));
  alert("Registration successful! You can now login.");
  showLogin();
}

// Login functionality
function login() {
  const username = document.getElementById("loginUsername").value;
  const password = document.getElementById("loginPassword").value;

  const storedData = localStorage.getItem(username);

  if (storedData) {
    const { email, password: storedPassword } = JSON.parse(storedData);
    if (password === storedPassword) {
      alert("Login successful! Welcome " + username);
    } else {
      alert("Incorrect password.");
    }
  } else {
    alert("User not found. Please register first.");
  }
}