async function registerUser() {
    const email = document.getElementById("email").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value;
  
    const res = await fetch("http://127.0.0.1:5000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, username, password, role })
    });
  
    const data = await res.json();
    document.getElementById("message").innerText = data.message || data.error;
  }
  
  async function loginUser() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
  
    const res = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });
  
    const data = await res.json();
    if (data.role === "admin") {
      localStorage.setItem("admin", data.username);
      window.location.href = "admin.html";
    } else if (data.role === "customer") {
      localStorage.setItem("customer", data.username);
      window.location.href = "customer.html";
    } else {
      document.getElementById("message").innerText = data.error || "Login failed.";
    }
  }
  