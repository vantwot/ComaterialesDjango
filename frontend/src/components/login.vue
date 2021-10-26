<template>
    <div class="logIn_user">
        <div class="container_logIn_user">
            <h2> Iniciar Sesión </h2>
            <form v-on:submit.prevent="processLogInUser"> <!-- PARA CUANDO SE DE ENVIAR AL FORMULACIO-->
                <input type="text" placeholder="username" v-model="user.username"> <!--esto es una entrada de texto, se puede cambiar para que sea boton o otra cosa, es una entrada-->
                <!--Placeholder, es un texto que se va a borrar al momento del usuario empezar a escribir en el campo.  v-model es basicamente una ayuda para hacer el objeto Javascript, lo que enviaremos en la peticion -->
                <br/> <!--SALTO DE LINEA-->
                <input type="password" placeholder="password" v-model="user.password">
                <br/>
                <button type="submit"> Iniciar sesión </button> 
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
                    'https://comateriales-be.herokuapp.com/login/', // endpoint al cual se envia
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
    .logIn_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
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
    .logIn_user h2{
        color: #283747;
    }
    .logIn_user form{
        width: 70%;
    }
    .logIn_user input{
        height: 40px;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;
        border: 1px solid #283747;
    }
    .logIn_user button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0;
    }
    .logIn_user button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }
</style>