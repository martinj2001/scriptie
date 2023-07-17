<template>
    <div id="accessibility">
        <ReadibilityOverall :data="data"/>
        <ReadibilityPerOrganization class="inline" :data="data" :class="{hide:!showOrganizations}"/>
        <ReadibilityColumn class="inline" :data="data" :class="{hide:!showFields}"/>
    </div>
</template>
  
<script>
import ReadibilityOverall from './ReadibilityOverall.vue';
import ReadibilityPerOrganization from './ReadibilityPerOrganization.vue';
import ReadibilityColumn from './ReadabilityColumn.vue';
    export default {
    name: 'Accessibility',
    components: {
    ReadibilityOverall,
    ReadibilityPerOrganization,
    ReadibilityColumn
},
    props: {
        data: Object,
        showOrganizations: Boolean,
        showFields: Boolean
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
