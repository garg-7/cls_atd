<template>
  <div>
    <div v-if="!attendanceData[0]" class="col-lg-12 col-md-12 col-sm-12 cell">
      <h2 class="ma-12">Upload the Image of Classroom to get Attendance</h2>
      <div v-if="imageURL">
        <v-img :src="imageURL" aspect-ratio="1.7"  max-width="85vh"></v-img>
      </div>
      <label>
        <input v-if ="!imageURL" type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
      <br>
      <v-btn v-if ="imageURL" large color="blue" class="ma-12 white--text" v-on:click="submitFile()">Submit</v-btn>
    </div>
    <div v-if="attendanceData[0]" class="col-md-6">
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
                    { text: 'Attendance', value: 'attendance'}
                ],
                attendanceData: [
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19DCS010',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    },
                    {
                        roll_no: 'MT19CS019',
                    }
                ]
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
                ).then(function(response){
                    console.log(response.data);
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
