<template>
  <div>
    <div v-if="!attendanceData[0].roll_no" class="col-lg-12 col-md-12 col-sm-12 cell">
      <h2 class="ma-12" >Upload the Image of Classroom to get Attendance</h2>
      <div v-if="imageURL">
        <v-img :src="imageURL" aspect-ratio="1.7"  max-width="85vh"></v-img>
      </div>
      <label v-if ="!imageURL" class="custom-file-upload">
        <input v-if ="!imageURL" type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        Upload a Image
      </label>
      <br>
      <v-btn v-if ="imageURL" large color="blue" :loading="loading" class="ma-12 white--text" v-on:click="submitFile()">Submit</v-btn>
    </div>
    <div v-if="attendanceData[0].roll_no" class="col-md-6">
      <v-data-table
          :headers="headers"
          :items="attendanceData"
          :items-per-page="30"
          class="elevation-1"
      ></v-data-table>
    </div>
    </div>
</template>

<script>
    import axios from "axios";
    export default {
        name: "ImageUpload",
        data(){
            return{
                image: '',
                imageURL: '',
                headers: [
                    { text: 'Roll no', value: 'roll_no' },
                    { text: 'Attendance', value: 'attendance'},
                    { text: 'Scores', value: 'scores'}
                ],
                loading : false,
                attendanceData: [{
                    roll_no : '',
                    attendance: '',
                    scores: ''
                }]
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
                this.loading = true;
                axios.post( 'api/image/',
                    formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }
                ).then((response)=>{
                    this.attendanceData = response.data;
                    this.loading = false;
                })
                    .catch(()=>{
                        console.log('FAILURE!!');
                    });


            }
        }

    }

</script>

<style scoped>
  input[type="file"] {
    display: none;
  }
  .custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
    background: blue;
    color: white;
  }
</style>
