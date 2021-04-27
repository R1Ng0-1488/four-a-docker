<template>
    <section>
        <div class="container">
        	<div class="row">
        		<div class="col-9 div m-3">
        			<h1 class="text-white border-danger">Добавить текст</h1>
        			<form class="text-white" method="post">
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Название</lable>
                            <div class="col-md-9">
                                <input type="text" name="title" class="form-control" placeholder="Название" required v-model="title"/>
                            </div>
                        </div>
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Текст</lable>
                            <div class="col-md-9">
                                <textarea name="text" cols="40" rows="10" class="form-control" placeholder="Текст" required v-model="text"></textarea>
                            </div>
                        </div>
        				<button class="btn btn-danger my-3" type="button" @click="sendTexts()">Спасти и Сохранить</button>
        			</form>
        		</div>
        	</div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'CreateTexts',
    data() {
        return {
            title: '',
            text: ''
        }
    },
    methods: {
        async sendTexts() {
            let data = {
                title: this.title,
                text: this.text
            }
            fetch(
                `${this.$store.getters.getServerUrl}/texts/create/`,
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                }
            ).then(response => {
                this.clearForm()
                this.$router.push({name: 'Texts'})
            })
        },
        clearForm() {
            title: this.title = ''
            text: this.text = ''
        }
    }
}
</script>
