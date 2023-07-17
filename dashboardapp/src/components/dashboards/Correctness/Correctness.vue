<template>
    <div id="correctness">
        <DateCorrectness class='inline' :data="data"/>
        <UrlCorrectness class='inline' :data="data"/>
        <EmailCorrectness class='inline' :data="data"/>
        <TypeCorrectness class='inline' :data="data"/>
    </div>
</template>
  
<script>
    import DateCorrectness from './DateCorrectness.vue';
    import UrlCorrectness from './UrlCorrectness.vue';
    import EmailCorrectness from './EmailCorrectness.vue';
    import TypeCorrectness from './TypeCorrectness.vue';
    export default {
    name: 'Correctness',
    components: {
    DateCorrectness,
    UrlCorrectness,
    EmailCorrectness,
    TypeCorrectness
},
    props: {
        data: Object
    },
    data() {
        return {}
    },
    mounted() {
    },
    methods: {

    }
}
</script>

<style scoped>
.inline {
    width: 25%;
    display: inline-block;
}
</style>
