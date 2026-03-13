import React, { useState } from "react";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    const response = await fetch(
      "http://127.0.0.1:5000/api/login",
      {
        method: "POST",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({ username, password }),
      },
    );

    const data = await response.json();
    if (response.ok) {
      setMessage(`Welcome, ${data.user.username}!`);
    } else {
      setMessage(data.message);
    }
  };
  return (
    <section>
      <div>
        <h2>Login</h2>
      </div>
      <div>
        <form onSubmit={handleLogin}>
          <div>
            <label htmlFor="username">Username*</label>
            <input
              type="text"
              name="username"
              id="username"
              className="border"
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <br />
          <div>
            <label htmlFor="password">Password*</label>
            <input
              type="text"
              name="password"
              id="password"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <div>
            <button type="submit">Login</button>
          </div>
        </form>
        {message && <p>{message}</p>}
      </div>
    </section>
  );
};

export default Login;
