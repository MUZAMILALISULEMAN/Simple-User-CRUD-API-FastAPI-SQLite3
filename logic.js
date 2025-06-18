    function showOutput(msg) {
      const out = document.getElementById("output");

      if (msg.data && Array.isArray(msg.data)) {
        if (msg.data.length === 0) {
          out.textContent = "No users found.";
          return;
        }

        out.innerHTML = msg.data.map(row => {
          const [id, name, age] = row;
          return `<div><b>ID:</b> ${id} | <b>Name:</b> ${name} | <b>Age:</b> ${age}</div>`;
        }).join("<hr>");
      } else if (typeof msg === "object") {
        out.textContent = Object.entries(msg).map(([k, v]) => `${k.toUpperCase()}: ${v}`).join("\n");
      } else {
        out.textContent = String(msg);
      }
    }

    document.getElementById("add-user").onclick = () => {
      let inp = document.getElementById("inpName").value;
      let inp2 = document.getElementById("inpAge").value;
      if (inp == "" || inp2 == "") return;

      fetch("https://simple-user-crud-api-fastapi-sqlite3.onrender.com/response/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: inp, age: Number(inp2) })
      })
      .then(response => response.json())
      .then(data => showOutput(data));
    }

    document.getElementById("show-user").onclick = () => {
      let inp3 = document.getElementById("inpId").value;
      if (inp3 == "") {
        fetch("https://simple-user-crud-api-fastapi-sqlite3.onrender.com/users")
          .then(response => response.json())
          .then(data => showOutput(data));
      } else {
        fetch(`https://simple-user-crud-api-fastapi-sqlite3.onrender.com/users/${inp3}`)
          .then(response => response.json())
          .then(data => showOutput(data));
      }
    }

    document.getElementById("delete-user").onclick = () => {
      let inp3 = document.getElementById("inpId").value;
      if (inp3 == "") return;

      fetch(`https://simple-user-crud-api-fastapi-sqlite3.onrender.com/del-user/${inp3}`, {
        method: "DELETE"
      })
      .then(response => response.json())
      .then(data => showOutput(data));
    }

    document.getElementById("update-user").onclick = () => {
      let id = document.getElementById("inpId").value;
      let name = document.getElementById("inpName").value;
      let age = document.getElementById("inpAge").value;
      if (!id || !name || !age) return;

      fetch(`https://simple-user-crud-api-fastapi-sqlite3.onrender.com/update-user/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, age: Number(age) })
      })
      .then(response => response.json())
      .then(data => showOutput(data));
    }
