const englishAlphabet = 'abcdefghijklmnopqrstuvxyz'.split('')

const getClipherMap = (alaphabet, shift) => {
    return alaphabet.
    reduce((charsMap, currentChar, charIndex) =>{
        const charsMapsClone = {...charsMap}

        let encrypytedCharIndex = (charIndex + shift) % alaphabet.length

        if(encrypytedCharIndex < 0){
            encrypytedCharIndex += alaphabet.length
        }

        charsMapsClone[currentChar] = alaphabet[encrypytedCharIndex]

        return charsMapsClone

    }, {})
}

const encrypt = (str, shift, alphabet = englishAlphabet) => {
    const cipherMap = getClipherMap(alphabet, shift)

    return str.toLowerCase().split('').map(char => cipherMap[char] || char).join('')
}

const dencrypt = (str, shift, alphabet = englishAlphabet) => {
    const cipherMap = getClipherMap(alphabet, -shift)

    return str.toLowerCase().split('').map(char => cipherMap[char] || char).join('')
}

const str = 'Hola mundo'
const enc = encrypt(str, 2)
const dec = dencrypt(str, 2)







