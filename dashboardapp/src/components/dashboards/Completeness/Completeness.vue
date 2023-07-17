<template>
    <div id="completeness">
        <CompleteTotal :data="data"/>
        <CompleteOrganization class="inline" :class={hide:!showOrganizations} :data="data"/>
        <CompleteColumn class="inline" :class="{hide:!showFields}" :data="data"/>
    </div>
</template>
  
<script>
    import CompleteTotal from './CompleteTotal.vue';
    import CompleteOrganization from './CompleteOrganization.vue';
    import CompleteColumn from './CompleteColumn.vue';
    export default {
    name: 'Completeness',
    components: {
        CompleteTotal,
        CompleteOrganization,
        CompleteColumn
    },
    props: {
        data: Object,
        showFields: Boolean,
        showOrganizations: Boolean
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
#completeness {
    width: 100%;
}

.inline {
    width: 49%;
    display: inline-block;
}


.hide {
    display: none;
}
</style>
