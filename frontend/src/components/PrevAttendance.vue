<template lang="pug">
  div.col-lg-6.ma-8
    v-btn.ma-6.white--text(color="blue" @click="goBack") Go Back
    div(v-if="dates[0]")
      v-select(:items="dates" label="Select Date" v-model="index" item-value="index" item-text="date" outlined)
    div(v-if="index!==-1")
      v-data-table.elevation-1(:headers="headers" :items="attendanceData[index]" :items-per-page="30")
</template>

<script>
    import { httpClient } from "../plugins/httpClient";
    export default {
        name: "PrevAttendance",
        data(){
            return{
                index: -1,
                dates: [],
                attendanceData: [],
                headers: [
                    { text: 'Roll no', value: 'student' },
                    { text: 'Attendance', value: 'status_display'}
                ]
            }
        },
        methods:{
            goBack(){
                this.$emit('current')
            }
        },
        mounted() {
            httpClient.get('api/attendance/').then(response=>{
                let data = response.data;
                data.forEach((ele,index)=>{
                    this.dates.push({
                        date: ele.date,
                        index: index
                    });
                    this.attendanceData.push(ele.attendance);
                })
            })
        }
    }
</script>

<style scoped>

</style>
