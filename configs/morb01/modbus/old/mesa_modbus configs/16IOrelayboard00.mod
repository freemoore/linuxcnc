/* Modbus definition file for a 16-channel relay board found on amazon geroosaty */

/*
The format of the channel descriptors is:

{TYPE, FUNC, ADDR, COUNT, pin_name}

TYPE is one of HAL_BIT, HAL_FLOAT, HAL_S32, HAL_U32
FUNC = 1, 2, 3, 4, 5, 6, 15, 16 - Modbus commands
COUNT = number of coils/registers to read
*/

#define MAX_MSG_LEN 40   // may be increased if necessary to max 251
#define DEBUG 1

static const hm2_modbus_chan_descriptor_t channels[] = {
/*  {TYPE,    FUNC, ADDR,   COUNT, pin_name} */
    {HAL_U32, 3,  0x0081, 16,       "IN"},
    {HAL_U32, 6,  0x0070, 1,     	"OUT00"},
    {HAL_U32, 6,  0x0071, 1,     	"OUT01"},
    {HAL_U32, 6,  0x0072, 1,     	"OUT02"},
    {HAL_U32, 6,  0x0073, 1,     	"OUT03"},
    {HAL_U32, 6,  0x0074, 1,     	"OUT04"},
    {HAL_U32, 6,  0x0075, 1,     	"OUT05"},
    {HAL_U32, 6,  0x0076, 1,     	"OUT06"},
    {HAL_U32, 6,  0x0077, 1,     	"OUT07"},
    {HAL_U32, 6,  0x0078, 1,     	"OUT08"},
    {HAL_U32, 6,  0x0079, 1,     	"OUT09"},
    {HAL_U32, 6,  0x007a, 1,     	"OUT10"},
    {HAL_U32, 6,  0x007b, 1,     	"OUT11"},
    {HAL_U32, 6,  0x007c, 1,     	"OUT12"},
    {HAL_U32, 6,  0x007d, 1,     	"OUT13"},
    {HAL_U32, 6,  0x007e, 1,     	"OUT14"},
    {HAL_U32, 6,  0x007f, 1,     	"OUT15"},

};


/* Optionally #define DEBUG to aid with troubleshooting.
   Use 3 to see a lot of information about the modbus
   internal workings. 1 is default (errors only)                    */

// vim: syn=c
