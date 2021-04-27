<template>
    <section>
        <div class="container">
        	<div class="row">
        		<div class="col-9 div m-3">
        			<h1 class="text-white border-danger">Добавить фотку</h1>
        			<form class="text-white" method="post">
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Название</lable>
                            <div class="col-md-9">
                                <input type="text" name="title" class="form-control" placeholder="Название" v-model="title"/>
                            </div>
                        </div>
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Ссылка на изображение</lable>
                            <div class="col-md-9">
                                <input type="url" name="image" class="form-control" placeholder="Ссылка на изображение" required v-model="image"/>
                            </div>
                        </div>
        				<button class="btn btn-danger my-3" type="button" @click="sendImages()">Спасти и Сохранить</button>
        			</form>
        		</div>
        	</div>
        </div>
    </section>
</template>

<script>
    export default {
        name: 'CreateImages',
        date() {
            return {
                title: '',
                image: ''
            }
        },
        methods: {
            async sendImages() {
                let data = {
                    title: this.title,
                    image: this.image
                }
                fetch(
                    `${this.$store.getters.getServerUrl}/images/create/`,
                    {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data)
                    }
                ).then(response => {
                    this.clearForm()
                    this.$router.push({name:'Images'})
                })
            },
            clearForm() {
                title: this.title = ''
                image: this.image = ''
            }
        }
    }
</script>
