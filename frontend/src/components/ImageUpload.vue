<template>
  <div class="container">
    <div class="col-lg-12 col-md-12 col-sm-12 cell">
      <label>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
    import axios from "axios";
    export default {
        name: "ImageUpload",
        data(){
            return{
                image: ''
            }
        },
        methods: {
            handleFileUpload() {
                this.image = this.$refs.file.files[0];
            },
            submitFile(){
                let formData = new FormData();
                formData.append('image', this.image);
                axios.post( 'api/image/',
                    formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }
                ).then(function(){
                    console.log('SUCCESS!!');
                })
                    .catch(function(){
                        console.log('FAILURE!!');
                    });


            }
        }

    }

</script>

<style scoped>

</style>
