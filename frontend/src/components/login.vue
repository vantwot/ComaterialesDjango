<template>
  <div class="logIn_user">
    <div class="container_logIn_user">
      <h2>Iniciar sesión</h2>
      <form v-on:submit.prevent="processLogInUser">
        <input type="text" v-model="user.username" placeholder="Username" />
        <br />
        <input type="password" v-model="user.password" placeholder="Password" />
        <br />
        <button type="submit">Iniciar Sesion</button>
      </form>
    </div>
  </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name:'logIn',
        data:function(){
            return {
                user:{
                    username:"",
                    password:""
                }
            }
        },

        methods:{
            // necesitamos 3 cosas para el axios 
            processLogInUser: function(){ 
                axios.post( // definir el metodo
                    'https://comateriales-be.herokuapp.com/user/login/', // endpoint al cual se envia
                    this.user, // la data o el Json que se envia
                    {HEADERS:{}} // LOS HEADERS ESTAN VACIOS
                )
                .then((result) => {// Esto se agrega para, al invocar la configuracion de endpoint, se va a ejecutar una serie de acciones, que son las que se colocan aca en el .then()
                    let dataLogin = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh:result.data.refresh
                    }
                
                    this.$emit('completedLogIn',dataLogin ) // emit es la forma en la que yo le voy a enviar informacion a la capa que está arriba (padre)
                })
                .catch((error) => {
                    if(error.response.status=="401"){alert("Las credenciales son incorrectas.")}
                })
            }
        },


    }

</script>

<style>
.logIn_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container_logIn_user {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 25%;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.logIn_user h2 {
  color: #283747;
}

.logIn_user form {
  width: 70%;
}
.logIn_user input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}
.logIn_user button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0;
}
.logIn_user button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>
<<<<<<< HEAD
=======

>>>>>>> dcf08851a2471db043d2f82dbaa42ca53fde3846
