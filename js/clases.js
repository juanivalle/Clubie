class Usuario {
    constructor(pNombre,pContraseña,pTipo,pEmail){
        this.nombre=pNombre;
        this.contraseña=pContraseña;
        // Tipo: 1 Club - 2 Cliente
        this.tipo = pTipo;
        this.email = pEmail
    }
}

class Plantas {
    constructor(pNombre, pEstado){
    this.nombre = pNombre
    this.estado = pEstado
    }
}

class Cogollos {
    constructor(pRaza,pStock,pPrecioU){
        this.raza = pRaza
        this.stock = pStock
        this.precio = pPrecioU
    }
}
