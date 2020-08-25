
//const { json } = require("express")
const express=require("express")
const app=express()
const fs=require("fs")
//const {execFile} = require("child_process")
app.use(express.json())
app.get("/get/:id",(req,res)=>{
	res.send(req.params)
})


app.post("/fuk/:id/req/:was", (req, res)=> {
	res.send(req.body)
	var a=req.body
	fs.appendFile("a.txt",`${JSON.stringify(a)}\n`)
    // execFile("./process.py",["-u","./a.txt"],(err,stdout,stderr)=>{
    //     console.log(stdout)
    // })

    //fs.writeFleSync("a.txt","A is here")    
})

app.listen(3000,()=>{
	console.log("Server listening")
})