<template>
    <v-container>
        <v-card>
            <v-card-title>
                <JsonExcel :data="cables" :fields="json_fields">
                    <v-btn>Download
                        <v-icon>mdi-download</v-icon>
                    </v-btn>
                </JsonExcel>
                <v-spacer></v-spacer>
                <v-text-field
                    class="col-4"
                    v-model="search"
                    append-icon="mdi-magnify"
                    label="Search"
                    single-line
                    hide-details
                ></v-text-field>
            </v-card-title>
            <v-data-table :headers="tableHeaders" :items="cables" :items-per-page="10" class="elevation-1" :search="search" dense >
                <template v-slot:body="props">
                    <tr>
                        <th></th>
                        <th></th>
                        <th v-for="(total, i) in totalStats" :key="`total-${i}`">{{total}}</th>
                    </tr>
                    <tr v-for="item in props.items" :key="item.id">
                        <td v-for="field in json_fields" :key="field">
                            <template v-if="field == 'id'">
                                <a target="_blank" :href="`http://www.geocaching.com/${item.link}`"> {{ item.id }} </a>
                            </template>
                            <template v-else-if="field == 'name'">
                                {{ item.name }}
                            </template>
                            <template v-else>
                                <template v-if="isBooleanColumn(field)">
                                    <v-icon v-if="getJsonDataForField(item, field, 0) >= 1" color="green">mdi-check</v-icon>
                                    <v-icon v-else color="red">mdi-close</v-icon>
                                </template>
                                <template v-else>
                                    <StatsChip :value="getJsonDataForField(item, field, 0)"/>
                                </template>
                            </template>
                        </td>
                    </tr>
                </template>
            </v-data-table>
        </v-card>
    </v-container>
</template>

<script>
import JsonExcel from "vue-json-excel"
import StatsChip from "@/components/StatsChip.vue"
export default {
    data() {
        return {
            search: '',
            json_fields: {
                'ID': 'id',
                'Name': 'name',
                'Logged Visits': 'logged_visits.total',
                'Found It': this.normalizeJsonDetailHeader('Found It'),
                'Didn\'t find it': this.normalizeJsonDetailHeader('Didn\'t find it'),
                'Write note': this.normalizeJsonDetailHeader('Write note'),
                'Needs Maintenance': this.normalizeJsonDetailHeader('Needs Maintenance'),
                'Owner Maintenance': this.normalizeJsonDetailHeader('Owner Maintenance'),
                'Update Coordinates': this.normalizeJsonDetailHeader('Update Coordinates'),
                'Will Attend': this.normalizeJsonDetailHeader('Will Attend'),
                'Announcement': this.normalizeJsonDetailHeader('Announcement'),
                'Attended': this.normalizeJsonDetailHeader('Attended'),
                'Archive': this.normalizeJsonDetailHeader('Archive'),
                'Unarchive': this.normalizeJsonDetailHeader('Unarchive'),
                'Webcam Photo': this.normalizeJsonDetailHeader('Webcam Photo'),
                'Temporarily Disable': this.normalizeJsonDetailHeader('Temporarily Disable'),
                'Enable Listing': this.normalizeJsonDetailHeader('Enable Listing'),
                'Retract Listing': this.normalizeJsonDetailHeader('Retract Listing'),
                'Submit for Review': this.normalizeJsonDetailHeader('Submit for Review'),
                'Permanently Archived': this.normalizeJsonDetailHeader('Permanently Archived'),
                'Needs Archived': this.normalizeJsonDetailHeader('Needs Archived'),
                'Publish Listing': this.normalizeJsonDetailHeader('Publish Listing'),
                'Post Reviewer': this.normalizeJsonDetailHeader('Post Reviewer')
            },
            cables: [
                {
                    "link": "/seek/cache_details.aspx?guid=c40f2862-8788-4b62-a917-b33415b8292c",
                    "name": "2. O primeiro tren de Galicia",
                    "id": "GC9G09K",
                    "logged_visits": {
                        "total": 5,
                        "detail": {
                            "found_it": 4,
                            "didnt_find_it": 0,
                            "write_note": 0,
                            "archive": 0,
                            "permanently_archived": 0,
                            "needs_archived": 0,
                            "will_attend": 0,
                            "attended": 0,
                            "webcam_photo": 0,
                            "unarchive": 0,
                            "temporarily_disable": 0,
                            "enable_listing": 0,
                            "publish_listing": 1,
                            "retract_listing": 0,
                            "needs_maintenance": 0,
                            "owner_maintenance": 0,
                            "update_coordinates": 0,
                            "post_reviewer": 0,
                            "announcement": 0,
                            "submit_for_review": 0
                        }
                    }
                },
                {
                    "link": "/seek/cache_details.aspx?guid=f4b62350-1771-4eb0-8cba-a599512ae170",
                    "name": "1. Cornes, a estaci\u00f3n de Rosal\u00eda",
                    "id": "GC9G3AK",
                    "logged_visits": {
                        "total": 0,
                        "detail": {
                            "found_it": 0,
                            "didnt_find_it": 0,
                            "write_note": 0,
                            "archive": 0,
                            "permanently_archived": 0,
                            "needs_archived": 0,
                            "will_attend": 0,
                            "attended": 0,
                            "webcam_photo": 0,
                            "unarchive": 0,
                            "temporarily_disable": 0,
                            "enable_listing": 0,
                            "publish_listing": 0,
                            "retract_listing": 0,
                            "needs_maintenance": 0,
                            "owner_maintenance": 0,
                            "update_coordinates": 0,
                            "post_reviewer": 0,
                            "announcement": 0,
                            "submit_for_review": 0
                        }
                    }
                },
                {
                    "link": "/seek/cache_details.aspx?guid=a1297718-49ad-4d5e-a782-323e756bcb93",
                    "name": "A mineir\u00eda compostelana",
                    "id": "GC949T0",
                    "logged_visits": {
                        "total": 33,
                        "detail": {
                            "found_it": 27,
                            "didnt_find_it": 3,
                            "write_note": 2,
                            "archive": 0,
                            "permanently_archived": 0,
                            "needs_archived": 0,
                            "will_attend": 0,
                            "attended": 0,
                            "webcam_photo": 0,
                            "unarchive": 0,
                            "temporarily_disable": 0,
                            "enable_listing": 0,
                            "publish_listing": 1,
                            "retract_listing": 0,
                            "needs_maintenance": 0,
                            "owner_maintenance": 0,
                            "update_coordinates": 0,
                            "post_reviewer": 0,
                            "announcement": 0,
                            "submit_for_review": 0
                        }
                    }
                },
                {
                    "link": "/seek/cache_details.aspx?guid=6168932d-3116-4e0e-9aa5-dac7bc1b2bb2",
                    "name": "Lume, auga e herbas",
                    "id": "GC935HM",
                    "logged_visits": {
                        "total": 21,
                        "detail": {
                            "found_it": 16,
                            "didnt_find_it": 4,
                            "write_note": 0,
                            "archive": 0,
                            "permanently_archived": 0,
                            "needs_archived": 0,
                            "will_attend": 0,
                            "attended": 0,
                            "webcam_photo": 0,
                            "unarchive": 0,
                            "temporarily_disable": 0,
                            "enable_listing": 0,
                            "publish_listing": 1,
                            "retract_listing": 0,
                            "needs_maintenance": 0,
                            "owner_maintenance": 0,
                            "update_coordinates": 0,
                            "post_reviewer": 0,
                            "announcement": 0,
                            "submit_for_review": 0
                        }
                    }
                },
                {
                    "link": "/seek/cache_details.aspx?guid=0a1f78cb-a4be-46cc-a71b-cc75ff3b6198",
                    "name": "Completa a Aventura LAB: Faite picheleiro",
                    "id": "GC92XH8",
                    "logged_visits": {
                        "total": 22,
                        "detail": {
                            "found_it": 21,
                            "didnt_find_it": 0,
                            "write_note": 0,
                            "archive": 0,
                            "permanently_archived": 0,
                            "needs_archived": 0,
                            "will_attend": 0,
                            "attended": 0,
                            "webcam_photo": 0,
                            "unarchive": 0,
                            "temporarily_disable": 0,
                            "enable_listing": 0,
                            "publish_listing": 1,
                            "retract_listing": 0,
                            "needs_maintenance": 0,
                            "owner_maintenance": 0,
                            "update_coordinates": 0,
                            "post_reviewer": 0,
                            "announcement": 0,
                            "submit_for_review": 0
                        }
                    }
                },
                {
                    "link": "/seek/cache_details.aspx?guid=15b43e1f-d5f1-489e-b1c2-3f464c49c9ee",
                    "name": "Ex\u00f3ticas no Xirimbao",
                    "id": "GC921GN",
                    "logged_visits": {
                        "total": 16,
                        "detail": {
                            "found_it": 15,
                            "didnt_find_it": 0,
                            "write_note": 0,
                            "archive": 0,
                            "permanently_archived": 0,
                            "needs_archived": 0,
                            "will_attend": 0,
                            "attended": 0,
                            "webcam_photo": 0,
                            "unarchive": 0,
                            "temporarily_disable": 0,
                            "enable_listing": 0,
                            "publish_listing": 1,
                            "retract_listing": 0,
                            "needs_maintenance": 0,
                            "owner_maintenance": 0,
                            "update_coordinates": 0,
                            "post_reviewer": 0,
                            "announcement": 0,
                            "submit_for_review": 0
                        }
                    }
                },
                {
                    "link": "/seek/cache_details.aspx?guid=405625d9-ea3e-451c-874a-a3b7339d8cbe",
                    "name": "Torre da Laxe",
                    "id": "GC90VKZ",
                    "logged_visits": {
                        "total": 5,
                        "detail": {
                            "found_it": 4,
                            "didnt_find_it": 0,
                            "write_note": 0,
                            "archive": 0,
                            "permanently_archived": 0,
                            "needs_archived": 0,
                            "will_attend": 0,
                            "attended": 0,
                            "webcam_photo": 0,
                            "unarchive": 0,
                            "temporarily_disable": 0,
                            "enable_listing": 0,
                            "publish_listing": 1,
                            "retract_listing": 0,
                            "needs_maintenance": 0,
                            "owner_maintenance": 0,
                            "update_coordinates": 0,
                            "post_reviewer": 0,
                            "announcement": 0,
                            "submit_for_review": 0
                        }
                    }
                },
                {
                    "link": "/seek/cache_details.aspx?guid=5d3b9e5f-d485-4ea3-b200-cbe5791ebd66",
                    "name": "Albergue do Cami\u00f1o Ingl\u00e9s",
                    "id": "GC8YPP9",
                    "logged_visits": {
                        "total": 39,
                        "detail": {
                            "found_it": 34,
                            "didnt_find_it": 0,
                            "write_note": 3,
                            "archive": 0,
                            "permanently_archived": 0,
                            "needs_archived": 0,
                            "will_attend": 0,
                            "attended": 0,
                            "webcam_photo": 0,
                            "unarchive": 0,
                            "temporarily_disable": 0,
                            "enable_listing": 0,
                            "publish_listing": 1,
                            "retract_listing": 0,
                            "needs_maintenance": 0,
                            "owner_maintenance": 1,
                            "update_coordinates": 0,
                            "post_reviewer": 0,
                            "announcement": 0,
                            "submit_for_review": 0
                        }
                    }
                }
            ]
        }
    },
    components: {
        JsonExcel,
        StatsChip
    },
    computed: {
        totalStats(){
            let total = []
            const keys = Object.keys(this.json_fields)
            for (let index = 2; index < keys.length; index++) {
                let value = 0
                const key = this.json_fields[keys[index]]
                for (const cable of this.cables) {
                    value += parseInt(this.getJsonDataForField(cable, key, 0))
                }
                total.push(value)
            }
            return total
        },
        tableHeaders(){
            let headers = []
            for (const key of Object.keys(this.json_fields)) {
                let header = { text: key, value: this.json_fields[key], align: 'center'}
                headers.push(header)
            }
            return headers
        }
    },
    methods: {
        getColor (logged) {
            return logged > 0 ? 'green' : 'gray'
        },
        getJsonDataForField(model, path, def) {
            path = path || ''
            model = model || {}
            def = typeof def === 'undefined' ? '' : def
            var parts = path.split('.')
            if (parts.length > 1 && typeof model[parts[0]] === 'object') {
                return this.getJsonDataForField(model[parts[0]], parts.splice(1).join('.'), def)
            } else {
                return model[parts[0]] || def
            }
        },
        isBooleanColumn(col){
            const booleanHeaders = ['Publish Listing', 'Permanently Archived'].map(this.normalizeJsonDetailHeader)
            return booleanHeaders.some(h => col.includes(h))
        },
        normalizeJsonDetailHeader(header){
            return `logged_visits.detail.${header.toLowerCase().replace(" ", "_").replace("'", "")}`
        }
    }
}
</script>

<style>
</style>