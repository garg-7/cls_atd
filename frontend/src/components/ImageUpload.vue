<template>
    <div class="col-lg-12 col-md-12 col-sm-12 cell">
      <div v-if="imageURL">
        <v-img :src="imageURL" aspect-ratio="1.7"  max-width="85vh"></v-img>
      </div>
      <label>
        <input v-if ="!imageURL" type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
      <br>
      <v-btn large color="blue" class="ma-12" v-on:click="submitFile()">Submit</v-btn>
    </div>
</template>

<script>
    import axios from "axios";
    export default {
        name: "ImageUpload",
        data(){
            return{
                image: '',
                imageURL: ''
            }
        },
        methods: {
            handleFileUpload() {
                this.image = this.$refs.file.files[0];
                this.imageURL = URL.createObjectURL(this.image);
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
