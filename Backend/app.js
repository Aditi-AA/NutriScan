const express=require("express");
const app=express();
const mongoose=require("mongoose");
app.use(express.json());

const mongoUrl="mongodb+srv://pfa2nd:QHJBuTHwoPLOWqVz@cluster0.jg69u.mongodb.net/AppData?retryWrites=true&w=majority&appName=Cluster0"

require('./models/UserDetails')
require('./models/SpecificCategory')
require("./models/Product")
require("./models/BarcodeInfo")

app.use(require('./routes/authentication'))
app.use(require('./routes/specificcat'))
app.use(require("./routes/products"))
app.use(require("./routes/barcodeinfo"))

app.get("/",(req,res)=>{
  res.send({status:"Started"})
})

mongoose.connect(mongoUrl).then(()=>{
  console.log("pfa2 mongodb connected")
}).catch((e)=>{
  console.log(e)
})



app.listen(5001,()=>{
    console.log("nodejs server started");
})