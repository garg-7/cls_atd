<template lang="pug">
  div
    div.col-lg-12.col-md-12.col-sm-12.cell(v-if="step===0")
      h2.ma-12 Upload the Image of Classroom to get Attendance
      div(v-if="imageURL")
        v-img(:src="imageURL" aspect-ratio="1.7" max-width="85vh")
      label.custom-file-upload(v-if="!imageURL")
        input(v-if="!imageURL" id="file" type="file" ref="file" v-on:change="handleFileUpload()")
        | Upload a Image
      br
      v-btn.ma-12.white--text(v-if="imageURL && !submitDone" large="" color="blue" :loading="loading" v-on:click="submitFile()") Submit
      v-btn.ma-12.white--text(v-if = "submitDone" large color="blue" @click = "step = 1") Check Results
    div.col-md-6(v-if="step===1")
      v-img(:src="markedImageURL" aspect-ratio="1.7" max-width="150vh")
      v-btn.ma-12.white--text( large color="blue" @click = "step = 2") Next
    div.col-md-6(v-if="step===2")
      v-data-table.elevation-1(v-model="selected"
        show-select item-key="score"
        :single-select="singleSelect"
        :headers="headersImg"
        :items="attendanceData"
        :items-per-page="30")
        template(v-slot:item.ref_img='{ item }')
          v-img.ma-2(:src="item.ref_img" max-height="10rem" max-width="10rem" height="auto" width="auto" )
        template(v-slot:item.ext_img='{ item }')
          v-img.ma-2(:src="item.ext_img" max-height="10rem" max-width="10rem" height="auto" width="auto")
        template(v-slot:top)
          v-btn.ml-12.white--text(large color="blue" @click = "step = 1") Go Back
          v-btn.ml-12.white--text(large color="blue" @click = "step = 3") Get Attendance
    div.col-md-6(v-if="step===3")
      v-data-table.elevation-1(:headers="headers" :items="selected" :items-per-page="30")
        template(v-slot:top)
            v-row(justify='center')
              v-dialog(v-model='dialog' max-width='290' persistent)
                template(v-slot:activator="{ on, attrs}")
                  v-btn.ma-1.white--text(large color="blue" @click = "step = 2") Go Back
                  v-btn.ma-1.white--text(large color='blue'
                    dark
                    @click.stop='dialog = true'
                    v-bind="attrs"
                    v-on="on" v-if="!saveDone") Save
                v-card(v-if = "!processing")
                  v-card-title.headline Are you Sure?
                  v-card-text Please confirm if you want to save the data.
                  v-card-actions
                    v-spacer
                    v-btn(color='green darken-1' text='' @click='dialog = false') Close
                    v-btn(color='green darken-1' text='' @click='saveData') Save
                v-card(v-else)
                  div.pa-10
                    v-progress-circular(:size="50", color="blue" indeterminate)
</template>

<script>
    import { httpClient } from "../plugins/httpClient";
    export default {
        name: "ImageUpload",
        data(){
            return{
                image: '',
                imageURL: '',
                markedImageURL: 'http://localhost:8000/static/output.jpg/',
                step: 0,
                singleSelect: false,
                submitDone: false,
                selected: [],
                studentList:[],
                headersImg: [
                    { text: 'Reference Image', value: 'ref_img'},
                    { text: 'Extracted Image', value: 'ext_img'},
                    { text: 'Scores', value: 'score'}
                ],
                headers: [
                    { text: 'Roll no', value: 'roll_no' },
                    { text: 'Attendance', value: 'attendance'},
                ],
                loading : false,
                attendanceData: [{
                    roll_no : '',
                    attendance: '',
                    score: '',
                    ref_img: '',
                    ext_img: '',
                }],
                dialog: false,
                saveDone: false,
                processing :false
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
                httpClient.post( 'api/image/',
                    formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }
                ).then((response)=>{
                    this.attendanceData = response.data;
                    this.loading = false;
                    this.submitDone = true;
                })
                    .catch(()=>{
                        console.log('FAILURE!!');
                    });
            },
            saveData(){
                this.processing = true;
                let data = [];
                let temp = [];
                this.selected.forEach(ele=>{
                    temp.push(ele.roll_no);
                    data.push({
                        student: ele.roll_no,
                        status: "1"
                    })
                });
                let absents = this.studentList.filter(ele=>{
                    return temp.indexOf(ele) < 0;
                });
                absents.forEach(ele =>{
                    data.push({
                        student: ele,
                        status: "2"
                    })
                });
                const list = {
                    attendance: data
                };
                httpClient.post('api/attendance/', list).then(() =>{
                    this.saveDone = true;
                    this.processing = false;
                    this.dialog = false;
                    location.reload();
                });
            }

        },
        mounted() {
            httpClient.get('api/students/').then(response=>{
                let data = response.data;
                data.forEach(ele=>{
                    this.studentList.push(ele.roll_no);
                })
            })
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
