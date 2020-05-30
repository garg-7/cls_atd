<template lang="pug">
  div
    div.col-lg-12.col-md-12.col-sm-12.cell(v-if="!attendanceData[0].roll_no")
      h2.ma-12 Upload the Image of Classroom to get Attendance
      div(v-if="imageURL")
        v-img(:src="imageURL" aspect-ratio="1.7" max-width="85vh")
      label.custom-file-upload(v-if="!imageURL")
        input(v-if="!imageURL" id="file" type="file" ref="file" v-on:change="handleFileUpload()")
      | Upload a Image
      br
      v-btn.ma-12.white--text(v-if="imageURL" large="" color="blue" :loading="loading" v-on:click="submitFile()") Submit
    div.col-md-6(v-if="attendanceData[0].roll_no")
      v-data-table.elevation-1(:headers="headers" :items="attendanceData" :items-per-page="30")
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
                    { text: 'Scores', value: 'score'}
                ],
                loading : false,
                attendanceData: [{
                    roll_no : '',
                    attendance: '',
                    score: ''
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
