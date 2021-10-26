<template>
  <body>
    <div class="main1">
      <p class="sign" align="center">Inicia sesión</p>
      <form v-on:submit.prevent="processLogInUser">
        <input
          class="un"
          type="text"
          placeholder="Usuario"
          v-model="user.username"
        />
        <input
          class="pass"
          type="password"
          placeholder="Contraseña"
          v-model="user.password"
        />
        <button class="submit" align="center">Entrar</button>
      </form>
    </div>
  </body>
</template>

<script>
import axios from "axios";
export default {
  name: "logIn",
  data: function () {
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    // necesitamos 3 cosas para el axios
    processLogInUser: function () {
      axios
        .post(
          // definir el metodo
          "https://comateriales-be.herokuapp.com/login/", // endpoint al cual se envia
          this.user, // la data o el Json que se envia
          { HEADERS: {} } // LOS HEADERS ESTAN VACIOS
        )
        .then((result) => {
          // Esto se agrega para, al invocar la configuracion de endpoint, se va a ejecutar una serie de acciones, que son las que se colocan aca en el .then()
          let dataLogin = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };

          this.$emit("completedLogIn", dataLogin); // emit es la forma en la que yo le voy a enviar informacion a la capa que está arriba (padre)
        })
        .catch((error) => {
          if (error.response.status == "401") {
            alert("Las credenciales son incorrectas.");
          }
        });
    },
  },
};
</script>

<style>
body {
    background-color: #FFFFFF;
    font-family: 'Ubuntu', sans-serif;
}
    
    .main1 {
        background-color: #FFFFFF;
        width: 400px;
        height: 300px;
        margin: 7em auto;
        border-radius: 1.5em;
        box-shadow: 0px 11px 35px 2px rgba(0, 0, 0, 0.14);
    }
    
    .sign {
        padding-top: 40px;
        color: #3f5237;
        font-family: 'Ubuntu', sans-serif;
        font-weight: bold;
        font-size: 23px;
    }
    
    .un {
    width: 76%;
    color: rgb(38, 50, 56);
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 1px;
    background: rgba(136, 126, 126, 0.04);
    padding: 10px 20px;
    border: none;
    border-radius: 20px;
    outline: none;
    box-sizing: border-box;
    border: 2px solid rgba(0, 0, 0, 0.02);
    margin-bottom: 50px;
    margin-left: 46px;
    text-align: center;
    margin-bottom: 27px;
    font-family: 'Ubuntu', sans-serif;
    }
    
    form.form1 {
        padding-top: 40px;
    }
    
    .pass {
            width: 76%;
    color: rgb(38, 50, 56);
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 1px;
    background: rgba(136, 126, 126, 0.04);
    padding: 10px 20px;
    border: none;
    border-radius: 20px;
    outline: none;
    box-sizing: border-box;
    border: 2px solid rgba(0, 0, 0, 0.02);
    margin-bottom: 50px;
    margin-left: 46px;
    text-align: center;
    margin-bottom: 27px;
    font-family: 'Ubuntu', sans-serif;
    }
    
   
    .un:focus, .pass:focus {
        border: 2px solid rgba(0, 0, 0, 0.18) !important;
        
    }
    
    .submit {
      cursor: pointer;
        border-radius: 5em;
        color: #fff;
        background:#3f5237;
        border: 0;
        padding-left: 40px;
        padding-right: 40px;
        padding-bottom: 10px;
        padding-top: 10px;
        font-family: 'Ubuntu', sans-serif;
        margin-left: 35%;
        font-size: 13px;
        box-shadow: 0 0 20px 1px rgba(0, 0, 0, 0.04);
    }
    
    .forgot {
        text-shadow: 0px 0px 3px rgba(117, 117, 117, 0.12);
        color: #E1BEE7;
        padding-top: 15px;
    }
    
    a {
        text-shadow: 0px 0px 3px rgba(117, 117, 117, 0.12);
        color: #E1BEE7;
        text-decoration: none
    }
    
    @media (max-width: 600px) {
        .main {
            border-radius: 0px;
        }
    }
        
</style>